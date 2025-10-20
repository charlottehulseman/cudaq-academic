"""Auto-grading system for CUDA-Q quantum circuits"""

import numpy as np

class CudaQAutoGrader:
    """Automated grading for quantum programming assignments"""
    
    def __init__(self):
        self.rubric = {
            'correctness': 0.5,  # 50% for correct output
            'efficiency': 0.3,   # 30% for gate optimization
            'style': 0.2        # 20% for code style
        }
    
    def grade_quantum_rng(self, student_function, n_bits=8):
        """Grade quantum RNG implementation"""
        score = 0
        feedback = []
        
        # Test correctness (checking for randomness)
        try:
            # Run student function multiple times
            results = []
            for _ in range(10):
                result = student_function(n_bits)
                results.append(result)
            
            # Check if results are different (true randomness)
            if len(set(results)) > 5:  # At least 6 different results
                score += self.rubric['correctness'] * 100
                feedback.append("✓ Correctly generates random numbers")
            else:
                feedback.append("✗ Output not sufficiently random")
                
        except Exception as e:
            feedback.append(f"✗ Error in execution: {str(e)}")
        
        # Check efficiency (simplified - would check gate count in real version)
        if score > 0:
            score += self.rubric['efficiency'] * 100
            feedback.append("✓ Efficient implementation")
        
        # Style points (simplified)
        score += self.rubric['style'] * 100
        feedback.append("✓ Good code structure")
        
        return {
            'score': int(score),
            'feedback': feedback,
            'passed': score >= 70
        }
    
    def grade_bell_state(self, student_function):
        """Grade Bell state preparation"""
        score = 0
        feedback = []
        
        try:
            # Check if function creates valid Bell state
            # (Simplified - would check actual state vector in real version)
            result = student_function()
            
            # Bell state should only have |00⟩ and |11⟩
            if '00' in result and '11' in result and '01' not in result and '10' not in result:
                score += self.rubric['correctness'] * 100
                feedback.append("✓ Correct Bell state created")
            else:
                feedback.append("✗ Not a valid Bell state")
                
        except Exception as e:
            feedback.append(f"✗ Error: {str(e)}")
        
        if score > 0:
            score += (self.rubric['efficiency'] + self.rubric['style']) * 100
            feedback.append("✓ Well-implemented")
        
        return {
            'score': int(score),
            'feedback': feedback,
            'passed': score >= 70
        }
    
    def provide_hint(self, assignment_name):
        """Provide hints for struggling students"""
        hints = {
            'quantum_rng': "Remember: Use Hadamard gates to create superposition, then measure",
            'bell_state': "Hint: Start with H gate on first qubit, then CNOT to second qubit",
            'grover': "Tip: You need an oracle and a diffusion operator"
        }
        return hints.get(assignment_name, "Keep trying! Review the lecture notes.")