from dataclasses import dataclass
from enum import Enum

class IdeaStatus(Enum):
    DRAFT = "Draft"
    IN_IDEATION = "In Ideation"
    VALIDATED = "Validated"
    REJECTED = "Rejected"

@dataclass
class Idea:
    id: int
    title: str
    description: str
    status: 'IdeaStatus'  # Use string here to avoid forward reference
    user_id: str

class IdeaManager:
    def __init__(self):
        self.ideas = {}

    def add_idea(self, user_id: str, title: str, description: str, status: 'IdeaStatus' = IdeaStatus.DRAFT) -> int:
        idea_id = len(self.ideas) + 1
        self.ideas[idea_id] = Idea(
            id=idea_id,
            title=title,
            description=description,
            status=status,
            user_id=user_id
        )
        return idea_id

    def get_all_ideas(self, user_id: str) -> list['Idea']:  # Use string here to avoid forward reference
        return [idea for idea in self.ideas.values() if idea.user_id == user_id]

    def update_status(self, idea_id: int, new_status: 'IdeaStatus') -> bool:  # Use string here to avoid forward reference
        if idea_id in self.ideas:
            self.ideas[idea_id].status = new_status
            return True
        return False
