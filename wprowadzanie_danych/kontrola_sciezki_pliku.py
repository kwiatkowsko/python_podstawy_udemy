import os
import datetime
data_input_catalog = r"c:\temp\data_input"
data_output_catalog = r"c:\temp\data_output"
today = datetime.date.today()
today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))

# checking conflicts

# input folder must exist
is_input_catalog_ok = os.path.isdir(data_input_catalog)

# output folder must exist
is_output_catalog_ok = os.path.isdir(data_output_catalog)

# today output catalog cannot exist
is_today_output_catalog_ok = not (os.path.isdir(today_output_catalog)) and \
                             not (os.path.isfile(today_output_catalog))

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('Prerequisites not met! Check the paths!')

    # display detailed error conditions
    if not is_input_catalog_ok:
        print("Input catalog %s must exist!" % data_input_catalog)
    if not is_output_catalog_ok:
        print("Output catalog %s must exist!" % data_output_catalog)
    if not is_today_output_catalog_ok:
        print("Today's output %s cannot exist (neither as file nor as directory)!" % today_output_catalog)
