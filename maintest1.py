# Filename: welcome_devops.py

def welcome_message(name, role):
    """
    Function to print a welcome message for a new DevOps job.
    
    Args:
    name (str): Name of the person
    role (str): The job title
    
    Returns:
    None
    """
    message = f"Hello {name}, welcome to your {role} job!"
    print(message)

# Main execution
if __name__ == "__main__":
    # Define user details
    user_name = "Arif"
    job_role = "DevOps"

    # Call the function to display the welcome message
    welcome_message(user_name, job_role)
