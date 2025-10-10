"""
title: Portkey Manifold Pipe
author: Portkey
version: 0.7.0
license: MIT
documentation: https://portkey.ai/docs/integrations/libraries/openwebui
"""

from pydantic import BaseModel, Field
from typing import Union, Generator, Iterator
import json
import requests


class Pipe:
    class Valves(BaseModel):
        PORTKEY_API_KEY: str = Field(
            default="",
            description="Your Portkey API key (required).",
        )
        PORTKEY_API_BASE_URL: str = Field(
            default="https://api.portkey.ai/v1",
            description="Base URL for Portkey API.",
        )
        AUTO_DISCOVER_MODELS: bool = Field(
            default=True,
            description="Auto-fetch models from Portkey.",
        )
        PORTKEY_MODELS: str = Field(
            default="@openai-slug/gpt-4o, @anthropic-slug/claude-sonnet-latest",
            description="Comma-separated model IDs (used when auto-discovery is off or as fallback).",
        )

    def __init__(self):
        self.type = "manifold"
        self.valves = self.Valves()
        self.name = "PORTKEY"

    def pipes(self) -> list:
        model_ids = []

        # Auto-discover models from Portkey
        if self.valves.AUTO_DISCOVER_MODELS and self.valves.PORTKEY_API_KEY:
            try:
                r = requests.get(
                    f"{self.valves.PORTKEY_API_BASE_URL}/models",
                    headers={"Authorization": f"Bearer {self.valves.PORTKEY_API_KEY}"},
                    timeout=10,
                )
                if r.status_code == 200:
                    data = r.json().get("data", [])
                    model_ids = [
                        m["id"] for m in data if isinstance(m, dict) and "id" in m
                    ]
            except:
                pass  # Fallback to manual list

        # Add manual models
        if self.valves.PORTKEY_MODELS:
            manual = [
                m.strip() for m in self.valves.PORTKEY_MODELS.split(",") if m.strip()
            ]
            model_ids.extend(manual)

        # Deduplicate
        seen = set()
        unique = []
        for m in model_ids:
            if m not in seen:
                seen.add(m)
                unique.append(m)

        return [{"id": m, "name": m} for m in unique]

    def pipe(self, body: dict, __user__: dict) -> Union[str, Generator, Iterator]:
        if not self.valves.PORTKEY_API_KEY:
            raise Exception("PORTKEY_API_KEY is required.")

        # Clean model ID (remove OpenWebUI prefix)
        full_model_id = body.get("model", "")
        actual_model_id = (
            full_model_id.split(".", 1)[-1] if "." in full_model_id else full_model_id
        )

        payload = {**body, "model": actual_model_id}

        # Build headers with metadata
        headers = {
            "Authorization": f"Bearer {self.valves.PORTKEY_API_KEY}",
            "Content-Type": "application/json",
        }

        metadata = {}
        if __user__:
            if "email" in __user__:
                metadata["email"] = __user__["email"]
            if "name" in __user__:
                metadata["name"] = __user__["name"]
            if "id" in __user__:
                metadata["user_id"] = __user__["id"]
            if "role" in __user__:
                metadata["role"] = __user__["role"]
            if "chat_id" in __user__:
                metadata["chat_id"] = __user__["chat_id"]

        if metadata:
            headers["x-portkey-metadata"] = json.dumps(metadata)

        try:
            r = requests.post(
                url=f"{self.valves.PORTKEY_API_BASE_URL}/chat/completions",
                json=payload,
                headers=headers,
                stream=body.get("stream", True),
            )
            r.raise_for_status()
            return r.iter_lines() if body.get("stream", True) else r.json()

        except requests.HTTPError as e:
            error_msg = f"Portkey API Error: {e.response.status_code}"
            try:
                error_details = e.response.json()
                error_msg += f" - {json.dumps(error_details)}"
            except:
                pass
            raise Exception(error_msg)

        except Exception as e:
            raise Exception(f"Error: {str(e)}")
