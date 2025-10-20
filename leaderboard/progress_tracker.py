"""
Real-time progress tracking and gamification
"""

import json
from datetime import datetime
from typing import List, Dict

class QuantumQuestTracker:
    def __init__(self, student_id: str):
        self.student_id = student_id
        self.points = 0
        self.level = 0
        self.badges = []
        self.completed_lessons = []
        self.help_given = 0
        
    def complete_lesson(self, lesson_id: str, score: int, time_taken: int):
        """Award points for lesson completion"""
        base_points = score
        
        # Time bonus
        if time_taken < self.get_time_limit(lesson_id):
            base_points += 25
            
        # First try bonus
        if lesson_id not in self.completed_lessons:
            base_points += 10
            
        self.points += base_points
        self.completed_lessons.append(lesson_id)
        self.check_level_up()
        
        return {
            'points_earned': base_points,
            'total_points': self.points,
            'level': self.level,
            'next_level_in': self.points_to_next_level()
        }
    
    def check_level_up(self):
        """Check if student leveled up"""
        level_thresholds = [0, 500, 1000, 2000, 3500, 5000]
        new_level = 0
        
        for i, threshold in enumerate(level_thresholds):
            if self.points >= threshold:
                new_level = i
                
        if new_level > self.level:
            self.level = new_level
            self.award_badge(f"Level_{new_level}_Badge")
            return True
        return False
    
    def can_join_hackathon(self) -> bool:
        """Check hackathon eligibility"""
        return self.level >= 3