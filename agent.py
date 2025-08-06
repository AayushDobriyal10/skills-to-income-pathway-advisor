import google.generativeai as genai

class IncomePathwayAdvisor:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        
    def generate_recommendations(self, user_input):
        prompt = f"""
        Act as a skill to pathway advisor. 
        User's skills: {user_input} Based on the users current_role , experience_level , education , location , target_salary , skills , interest
        suggest job opportunities in their field. Provide income ranges where possible. keep it concise.
        Response Format:

        Income Projection based on your location and target skills:
        [Projected salary based on user's target skills, location, and experience level]

        job opportunities:

        Job  #1: [job name]

        Growth Projection: [Market growth percentage]

        Key Skills: [Related skills to acquire]

        Expected Salary: [Projected salary range]

        RoadMap : [road map for job]

        job #2: [job name]

        Growth Projection: [Market growth percentage]

        Key Skills: [Related skills to acquire]

        Expected Salary: [Projected salary range]

        RoadMap : [road map for job]

        job #3: [job name]

        Growth Projection: [Market growth percentage]

        Key Skills: [Related skills to acquire]

        Expected Salary: [Projected salary range]

        RoadMap : [road map for job]

        Market Insight for your location:

        Location: [User's location]

        Market growth: [Market demand, potential salary trends, and growth in the user's field]

        Salary Comparison: [National average vs. location's salary trends]

        Key Constraints:

        Keep responses concise and stick to the provided format.

        Focus on actionable insights: salary projections, skills, and market insights.

        Avoid unnecessary details or long explanations.
        """
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)

        return response.text.strip()

    def suggest_income_pathways(self, current_role , experience_level , education , location , target_salary , skills , interest):

        user_input = f""" current role : {current_role},
        Experience Level: {experience_level},
        education: {education}, 
        location: {location} , 
        target salary : {target_salary},
        skills : {skills},
        interest : {interest}
        """
        
        recommendations = self.generate_recommendations(user_input)
        pathway = recommendations.strip()
        return pathway

def get_user_input():
    current_role = input("Enter your current role : ").strip()
    experience_level = input("Enter your experience level : ").strip()
    education = input("Enter your education level: ").strip()
    location = input("Enter your desired location : ").strip()
    target_salary = input("Enter your target salary : ").strip()
    skills = input('Enter your current skills : ')
    interest = input('Enter your interests :')
    
    return current_role , experience_level , education , location , target_salary , skills , interest

advisor = IncomePathwayAdvisor(api_key="AIzaSyA8DBdo1xImKlkjziL_AFjm01PDMOR4rU0")
current_role , experience_level , education , location , target_salary , skills , interest = get_user_input()
    
recommendations = advisor.suggest_income_pathways(current_role , experience_level , education , location , target_salary , skills , interest)
    
print("\nSuggested Income Pathways:")
print(recommendations)
