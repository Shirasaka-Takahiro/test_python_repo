import os
import subprocess

#Define AWS environment variables
def set_aws_environment_variables():
    os.environ["AWS_ACCESS_KEY_ID"] = input("Set AWS_ACCESS_KEY_ID:")
    os.environ["AWS_SECRET_ACCESS_KEY"] = input("Set AWS_SECRET_ACCESS_KEY: ")
    os.environ["AWS_DEFAULT_REGION"] = input("Set AWS_DEFAULT_REGION: ")

#Define execution command
def exec_terraform_command(command, directory, output_file=None):
    current_directory = os.getcwd()

    try:
        os.chdir(directory)

        if output_file:
            with open(output_file, "w") as file:
                subprocess.run(command, shell=True, check=True, stdout=file)
        else:
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command execution faild: {e}")
    finally:
        os.chdir(current_directory)

#Set a directory where terraform command should be executing
target_directory = "/home/takahiro/terraform/alb_ec2x1_route53_terraform/env/dev"

def main():

    while True:
        print("1. Set AWS environment variables")
        print("2. Terraform init")
        print("3. Terraform plan")
        print("4. Terraform apply")
        print("5. Execute 1-3 command above")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            set_aws_environment_variables()

        elif choice == "2":
            command_to_exec_init = "terraform init"
            output_file = "/home/takahiro/test_python/exec_terraform/output.txt"
            exec_terraform_command(command_to_exec_init, target_directory, output_file)
            print("Successfully initiated!")

        elif choice == "3":
            command_to_exec_plan = "terraform plan"
            exec_terraform_command(command_to_exec_plan, target_directory)
            print("Successfully completed!")

        elif choice == "4":
            command_to_exec_apply = "terraform apply"
            exec_terraform_command(command_to_exec_apply, target_directory)
            print("Successfully applied!")

        elif choice == "5":
            command_to_exec_init = "terraform init"
            output_file = "/home/takahiro/test_python/exec_terraform/output.txt"
            exec_terraform_command(command_to_exec_init, target_directory, output_file)
            command_to_exec_plan = "terraform plan"
            exec_terraform_command(command_to_exec_plan, target_directory)
            command_to_exec_apply = "terraform apply"
            exec_terraform_command(command_to_exec_apply, target_directory)
            print("Successfully applied!")

        elif choice == "6":
            print("Exiting...BYE")
            break

        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()