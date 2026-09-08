from logger_utils import Logger

logger = Logger()
#Day 1 with try except and finally only
#Day2 using logging module

try:

    logger.info("Starting the logging process")
    with open("app.txt", "r") as file:
        lines = file.readlines()

    logger.info("Input file read successfully")

    error_Lines = []

    for line in lines:
        if "ERROR" in line:
            error_Lines.append(line)
            if (error_Lines):
                    logger.info(f"Error lines found: {len(error_Lines)} Error Lines")

    with open("error_txt", "w+") as file:
        file.writelines(error_Lines)

    logger.info("Error lines written successfully")
    logger.info("Bot runned successfully")
    
except FileNotFoundError:
    logger.error("Log file not found")
except Exception as e:
    logger.error(f"An error occurred: {e}")
finally:
   logger.info("Processing completed")
        








       
