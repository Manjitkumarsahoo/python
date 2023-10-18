#EXCEPTION HANDLING

def calculate_avg_from_file(file_path):
    try:
        with open(file_path,"r") as file:
            total=0
            count=0
            for line in file:
                try:
                 number=float(line.strip())
                 total +=number
                 count+=1
                except ValueError:
                   print("invalid dat found in the file")

            if count==0:
               raise ValueError("no valid data found in the file.")
            average=total/count
            return average
    except FileNotFoundError:
       print("error: the file'{}' was not found",format(file_path))
    except PermissionError:
       print("Error: Permission denied to access the file '{}'.".format(file_path))
    except Exception as e:
       print("Error: An unexpected error occurred -", str(e))
    else:
       print("calculation successful")
    finally:
       print("operation complet")

file_path="data.txt"
average=calculate_avg_from_file(file_path)
if average is not None:
   print("Average",average)
else:
   print("unable to calculate average")
                   
