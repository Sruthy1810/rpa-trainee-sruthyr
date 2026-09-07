try:
    with open("app.log", "r") as file:
        lines = file.readlines()
        error_Lines = []

    for line in lines:
        if "Error" in line:
            error_Lines.append(line)

    with open("error_txt", "w") as file:
        file.writelines(error_Lines)

except FileNotFoundError:
    print("Log file not found")
except Exception as e:
    print(f"Ann error occured: {e}")
finally:
    print("Processing completed")
        








    print("Processing completed.")    
