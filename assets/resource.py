"""
Sometimes, the given expected score for Bodhitree quizzes is different from the actual expected score. This is because
(Bodhitree is shit) the number of attempts/scores fluctuate or the content gets boom! So to balance those changes, a per subject fluctuation has to be maintained.
And this is what this balance dictionary is about!
The format is "Subject-Name" : [out video score fluctuation, in video score fluctuation]
For e.g., in the DM course of Div. A and B, the actual attainable out video score is 59, whereas the given max out video score is 60. This fluctuation is noted here.
"""

balance = {
    "Discrete Mathematics SE Comp A & B": [1, 0],
    "Object Oriented Programming using C++ , Division B and D": [0, 0],
    "Fundamental of Data Structures": [0, 7],
    "Computer Graphics Lab (Div - B)": [1, 0],
    "Humanity and Social Science": [0, 0],
    "Digital Electronics Lab ( SE COMP B Division)": [10, 3],
    "Data Structure Laboratory_SE_B": [0, 1],
    "DELD Theory SE COMP Div B-Dr. Ranjanikar": [0, 0],
    "Computer Graphics": [0, 0],
}
