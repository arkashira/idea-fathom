import csv
import itertools
from dataclasses import dataclass, field
from io import StringIO
from typing import Dict, List, Optional


@dataclass
class Idea:
    """Represents a single idea."""
    id: int
    title: str
    validation_score: Optional[float] = None

    @property
    def validated(self) -> bool:
        return self.validation_score is not None


class IdeaFathomDashboard:
    """
    Core logic for the Idea‑Fathom dashboard.

    It tracks ideas, their validation scores and provides aggregated metrics.
    """

    _id_counter = itertools.count(1)

    def __init__(self) -> None:
        self._ideas: Dict[int, Idea] = {}

    # --------------------------------------------------------------------- #
    # Public API
    # --------------------------------------------------------------------- #

    def add_idea(self, title: str) -> int:
        """
        Add a new idea and return its unique identifier.

        Args:
            title: Human‑readable title of the idea.

        Returns:
            The generated integer id.
        """
        if not isinstance(title, str) or not title:
            raise ValueError("title must be a non‑empty string")
        idea_id = next(self._id_counter)
        self._ideas[idea_id] = Idea(id=idea_id, title=title)
        return idea_id

    def validate_idea(self, idea_id: int, score: float) -> None:
        """
        Record a validation score for an existing idea.

        Args:
            idea_id: Identifier returned by :meth:`add_idea`.
            score: Validation score; must be a non‑negative number.

        Raises:
            KeyError: If ``idea_id`` does not exist.
            ValueError: If ``score`` is negative.
        """
        if score < 0:
            raise ValueError("validation score must be non‑negative")
        try:
            idea = self._ideas[idea_id]
        except KeyError as exc:
            raise KeyError(f"Idea id {idea_id} not found") from exc
        idea.validation_score = float(score)

    def total_ideas(self) -> int:
        """Return the total number of ideas added."""
        return len(self._ideas)

    def validated_ideas(self) -> int:
        """Return the count of ideas that have a validation score."""
        return sum(1 for i in self._ideas.values() if i.validated)

    def average_validation_score(self) -> float:
        """
        Compute the average validation score across validated ideas.

        Returns:
            The average as a float; ``0.0`` when no ideas are validated.
        """
        scores = [i.validation_score for i in self._ideas.values() if i.validated]
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    def get_stats(self) -> Dict[str, float]:
        """
        Convenience method returning all three dashboard metrics.

        Returns:
            Mapping with keys ``total``, ``validated`` and ``average_score``.
        """
        return {
            "total": self.total_ideas(),
            "validated": self.validated_ideas(),
            "average_score": self.average_validation_score(),
        }

    def export_csv(self) -> str:
        """
        Export the current idea list as a CSV string.

        Columns:
            id, title, validated (bool), validation_score (empty if not validated)

        Returns:
            CSV formatted text.
        """
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "title", "validated", "validation_score"])
        for idea in self._ideas.values():
            writer.writerow([
                idea.id,
                idea.title,
                str(idea.validated),
                "" if not idea.validated else f"{idea.validation_score:.2f}",
            ])
        return output.getvalue()
