from __future__ import annotations
from dataclasses import dataclass
from openai import OpenAI

@dataclass
class ExpertAgent:
    name: str
    instructions: str
    client: OpenAI | None
    model: str

    def review(self, task: str, knowledge: str) -> str:
        if self.client is None:
            raise RuntimeError("OpenAI-API-Client ist nicht konfiguriert.")
        prompt = f"""
Du bist der Experte: {self.name}

Unternehmenswissen, Governance und Board-Kontext:
{knowledge}

Zu bewertende Aufgabe, Anforderung oder Managementfrage:
{task}

Erstelle eine strukturierte Expertenbewertung mit:
1. Kernaussage
2. Chancen
3. Risiken
4. Anforderungen
5. Konkrete Empfehlungen
6. Offene Fragen
"""
        response = self.client.responses.create(
            model=self.model,
            instructions=self.instructions,
            input=prompt,
        )
        return response.output_text
