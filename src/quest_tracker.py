"""Progress tracking and gamification system"""

class QuantumQuestProgress:
    """Track student progress through quantum learning journey"""
    
    LEVEL_THRESHOLDS = {
        0: (0, "🌱 Quantum Initiate"),
        1: (100, "🎲 Superposition Explorer"),
        2: (300, "🔗 Entanglement Engineer"),
        3: (500, "🔍 Algorithm Apprentice"),
        4: (700, "💊 Application Architect"),
        5: (1000, "🚀 Optimization Oracle")
    }
    
    def __init__(self, student_name):
        self.name = student_name
        self.points = 0
        self.level = 0
        self.badges = []
        self.completed_lessons = []
        self.hackathon_eligible = False
        
    def complete_lesson(self, lesson_name, base_score, time_taken=None, time_limit=None):
        """Award points for completing a lesson"""
        total_score = base_score
        
        # Time bonus
        if time_taken and time_limit and time_taken < time_limit:
            total_score += 25
            print(f"⚡ Speed bonus! +25 points")
        
        # First completion bonus
        if lesson_name not in self.completed_lessons:
            total_score += 10
            self.completed_lessons.append(lesson_name)
        
        self.points += total_score
        old_level = self.level
        
        # Check level up
        for lvl, (threshold, badge_name) in self.LEVEL_THRESHOLDS.items():
            if self.points >= threshold:
                self.level = lvl
                
        if self.level > old_level:
            badge = self.LEVEL_THRESHOLDS[self.level][1]
            self.badges.append(badge)
            print(f"\n🎉 LEVEL UP! You are now: {badge}")
            
            if self.level >= 3 and not self.hackathon_eligible:
                self.hackathon_eligible = True
                print("\n✨ HACKATHON UNLOCKED!")
                print("📍 You can now form a team for the NVIDIA Quantum Challenge!")
        
        return total_score
    
    def get_progress_bar(self):
        """Visual progress bar"""
        if self.level < 5:
            next_threshold = self.LEVEL_THRESHOLDS[self.level + 1][0]
            current_threshold = self.LEVEL_THRESHOLDS[self.level][0]
            progress = (self.points - current_threshold) / (next_threshold - current_threshold)
            bar_length = 20
            filled = int(bar_length * progress)
            bar = '█' * filled + '░' * (bar_length - filled)
            return f"[{bar}] {int(progress*100)}% to Level {self.level + 1}"
        return "[████████████████████] MAX LEVEL"
    
    def display_status(self):
        """Display current status"""
        print(f"\n🎮 {self.name}'s Quantum Quest Status")
        print("=" * 50)
        print(f"📊 Points: {self.points}")
        print(f"🏆 Level: {self.level} - {self.LEVEL_THRESHOLDS[self.level][1]}")
        print(f"📈 Progress: {self.get_progress_bar()}")
        print(f"🎯 Completed: {len(self.completed_lessons)} lessons")
        print(f"🏅 Badges: {len(self.badges)}")
        
        if not self.hackathon_eligible:
            needed = 500 - self.points
            print(f"\n→ {needed} points to unlock hackathon")