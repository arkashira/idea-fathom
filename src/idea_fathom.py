import json
from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    concept: str
    market_size: int
    competition: int

class IdeaFathom:
    def __init__(self, knowledge_base: List[Idea]):
        self.knowledge_base = knowledge_base

    def validate_idea(self, idea: Idea) -> dict:
        """Validate an idea against the knowledge base"""
        duplicate = any(idea.concept == existing_idea.concept for existing_idea in self.knowledge_base)
        if duplicate:
            return {"valid": False, "reason": "Duplicate concept"}
        
        # Simple validation metrics
        market_size_valid = idea.market_size > 0
        competition_valid = idea.competition > 0
        
        return {
            "valid": market_size_valid and competition_valid,
            "metrics": {
                "market_size": idea.market_size,
                "competition": idea.competition
            }
        }

    def add_idea_to_knowledge_base(self, idea: Idea):
        """Add a validated idea to the knowledge base"""
        self.knowledge_base.append(idea)
