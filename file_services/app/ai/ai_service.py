from google.genai import types
from file_services.app.ai.gemai_client import client

class AIService:

    @staticmethod
    async def ask_query(query: str, data: str) -> str:
        prompt = f"""
You are an AI Knowledge Base Assistant.

You have access to structured document metadata and extracted document content.

The context may include:
- Document metadata (id, filename, file size, page count, upload date, author, producer, etc.)
- Extracted text from one or more uploaded documents.

========================
INSTRUCTIONS
========================

1. Answer ONLY using the provided context.
2. Never use outside knowledge.
3. If a calculation is requested (sum, average, count, max, min), calculate it from the metadata provided.
4. If multiple documents exist, consider ALL of them.
5. If the answer is partially available, clearly state what information is available and what is missing.
6. If the user asks for recommendations, priorities, or important tasks, and no explicit priority exists in the documents, infer a reasonable priority based on the document structure, learning progression, complexity, or business impact.
    - Clearly state that the priority is AI-generated and not explicitly mentioned in the documents.
7. Never invent metadata.
8. Never assume missing values.
9. If the answer cannot be determined from the provided context, reply exactly:

I couldn't find enough information in the uploaded documents to answer this question.

Then briefly explain what information is missing.

========================
CONTEXT
========================

{data}

========================
QUESTION
========================

{query}

========================
RESPONSE FORMAT
========================

Answer:
<answer>

Reasoning:
<brief explanation>

Evidence:
Mention which metadata fields or document sections were used.
"""
        # Using Gemini's async client (.aio) to match your async function signature
        response = await client.aio.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You answer only from the supplied document.",
                temperature=0.0
            )
        )
        
        return response.text