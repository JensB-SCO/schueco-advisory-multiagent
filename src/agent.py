from __future__ import annotations
from dataclasses import dataclass
from openai import OpenAI

@dataclass
class ExpertAgent:
    name: str
    instructions: str
    client: OpenAI
    model: str

    def review(self, task: str, knowledge: str) -> str:
        prompt = f"""
Du bist der Experte: {self.name}

Unternehmens- und Projektwissen:
{knowledge}

Aufgabe:
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
