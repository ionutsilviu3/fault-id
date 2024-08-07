import pandas as pd
import random
import datetime

# Function to generate serials
def generate_serials(start_day, end_day, num_serials):
    
    serials = []
    current_day = start_day
    serial_id = 1
    
    # Loop over the specified timeframe
    while current_day <= end_day and len(serials) < num_serials:
        for hour in range(24):
            for minute in range(0, 60, random.choice([4, 5, 6])):  # Generate serials at random intervals
                # Generate random hour and minute
                rand_hour = str(hour).zfill(2)
                rand_minute = str(minute).zfill(2)
                
                # Generate serial for each serial type
                serial_types = [('FP', 1), ('IV', 2), ('BS', 3)]  # Fuel Pump, Power Inverter, Brake Sensor
                for serial_type, serial_type_id in serial_types:
                    serial = f"{serial_type}{serial_type_id}D{current_day.strftime('%y%m%d')}T{rand_hour}{rand_minute}I{serial_id}"
                    serials.append((serial, serial_type_id, datetime.datetime.strptime(f"{current_day.strftime('%y%m%d')} {rand_hour}{rand_minute}", '%y%m%d %H%M')))
                    serial_id += 1
                    
                    if len(serials) >= num_serials:
                        break
                
                if len(serials) >= num_serials:
                    break
            
            if len(serials) >= num_serials:
                break
        
        current_day += datetime.timedelta(days=1)
    
    return serials

# Function to generate process events, results, limits, and parameters
def generate_data(serial_df):
    
        # Predefined parameters and limits
    parameters_data = [
        {'name': 'Voltage', 'unit_of_measurement': 'V'},
        {'name': 'Current Draw', 'unit_of_measurement': 'A'},
        {'name': 'Resistance', 'unit_of_measurement': 'ohm'},
        {'name': 'Motor RPM', 'unit_of_measurement': 'RPM'},
        {'name': 'Pressure', 'unit_of_measurement': 'psi'},
        {'name': 'Flow Rate', 'unit_of_measurement': 'liters per hour'},
        {'name': 'Efficiency', 'unit_of_measurement': '%'},
        {'name': 'Sound Levels', 'unit_of_measurement': 'dB(A)'},
        {'name': 'Harmonic Distortion', 'unit_of_measurement': '%'},
        {'name': 'Operating Temperature', 'unit_of_measurement': '°C'}
    ]

    limits_data = [
        {'parameter_id': 1, 'serial_type_id': 1, 'lower_limit': 11.4, 'upper_limit': 12.6, 'created_at': '2019-02-21 00:00:00'},
        {'parameter_id': 2, 'serial_type_id': 1, 'lower_limit': 4.75, 'upper_limit': 15.25, 'created_at': '2019-03-12 00:00:00'},
        {'parameter_id': 3, 'serial_type_id': 1, 'lower_limit': 0, 'upper_limit': 0.95, 'created_at': '2019-06-24 00:00:00'},
        {'parameter_id': 4, 'serial_type_id': 1, 'lower_limit': 1900, 'upper_limit': 6100, 'created_at': '2019-08-24 00:00:00'},
        {'parameter_id': 5, 'serial_type_id': 1, 'lower_limit': 28.5, 'upper_limit': 81.5, 'created_at': '2019-08-24 00:00:00'},
        {'parameter_id': 6, 'serial_type_id': 1, 'lower_limit': 95, 'upper_limit': 205, 'created_at': '2019-09-28 00:00:00'},
        {'parameter_id': 7, 'serial_type_id': 1, 'lower_limit': 69.5, 'upper_limit': 100, 'created_at': '2019-10-13 00:00:00'},
        {'parameter_id': 8, 'serial_type_id': 1, 'lower_limit': 0, 'upper_limit': 66.5, 'created_at': '2019-11-04 00:00:00'},
        {'parameter_id': 9, 'serial_type_id': 1, 'lower_limit': 0, 'upper_limit': 4.75, 'created_at': '2019-11-18 00:00:00'},
        {'parameter_id': 10, 'serial_type_id': 1, 'lower_limit': -42, 'upper_limit': 122, 'created_at': '2019-12-07 00:00:00'}
    ]
    process_events = []
    results = []

    # Loop through each row in the serial DataFrame
    for index, row in serial_df.iterrows():
        serial_id = row['id']
        serial_type_id = row['serial_type_id']
        created_at = row['created_at']

        # Generate process events for each station
        for station_id, station_name in [(1, "S100"), (2, "S120"), (3, "S150"), (4, "S200")]:
            # Define process event
            process_event = {
                "event_type_id": 2,
                "serial_id": serial_id,
                "station_id": station_id,
                "start_time": created_at - datetime.timedelta(minutes=3),  # Start time 3 minutes before serial creation
                "end_time": created_at
            }
            process_events.append(process_event)

            # Generate results for each parameter
            for parameter_id, parameter_data in enumerate(parameters_data, start=1):
                lower_limit = next(limit['lower_limit'] for limit in limits_data if limit['parameter_id'] == parameter_id)
                upper_limit = next(limit['upper_limit'] for limit in limits_data if limit['parameter_id'] == parameter_id)
                
                # Generate result
                value = random.uniform(lower_limit, upper_limit)
                result = {
                    "event_id": len(process_events),  # Use the index of the process event
                    "parameter_id": parameter_id,
                    "value": value,
                    "created_at": created_at
                }
                results.append(result)

    return process_events, results

# TODO remove, used for temp inserts
    def boilerplate():

        pass
        # TODO remove, used for temp inserts
        # df = self.client.execute_query(self.query_master.get_process_events())
        # print(df)
        # r = self.generate_results(df)
        # results = pd.DataFrame(r)
        # self.replace_results_table(results)

        # serials = self.client.execute_query(self.client.query_master.get_serials())
        # serials = serials[serials['serial_type_id'] == 1]

        # process_events, results = models.create_serials_script.generate_data(serials)

        # process_event_chunks = [process_events[i:i+1000] for i in range(0, len(process_events), 1000)]
        # result_chunks = [results[i:i+1000] for i in range(0, len(results), 1000)]

        # for chunk in process_event_chunks:
        #     self.client.insert_process_events(chunk)
        # for chunk in result_chunks:
        #     self.client.insert_results(chunk)
    def generate_results(self, process_events_df):
        results = []

        # Predefined parameters and limits
        parameters_data = [
            {'name': 'Voltage', 'unit_of_measurement': 'V'},
            {'name': 'Current Draw', 'unit_of_measurement': 'A'},
            {'name': 'Resistance', 'unit_of_measurement': 'ohm'},
            {'name': 'Motor RPM', 'unit_of_measurement': 'RPM'},
            {'name': 'Pressure', 'unit_of_measurement': 'psi'},
            {'name': 'Flow Rate', 'unit_of_measurement': 'liters per hour'},
            {'name': 'Efficiency', 'unit_of_measurement': '%'},
            {'name': 'Sound Levels', 'unit_of_measurement': 'dB(A)'},
            {'name': 'Harmonic Distortion', 'unit_of_measurement': '%'},
            {'name': 'Operating Temperature', 'unit_of_measurement': '°C'}
        ]

        limits_data = [
            {'parameter_id': 1, 'lower_limit': 11.4, 'upper_limit': 12.6},
            {'parameter_id': 2, 'lower_limit': 4.75, 'upper_limit': 15.25},
            {'parameter_id': 3, 'lower_limit': 0, 'upper_limit': 0.95},
            {'parameter_id': 4, 'lower_limit': 1900, 'upper_limit': 6100},
            {'parameter_id': 5, 'lower_limit': 28.5, 'upper_limit': 81.5},
            {'parameter_id': 6, 'lower_limit': 95, 'upper_limit': 205},
            {'parameter_id': 7, 'lower_limit': 69.5, 'upper_limit': 100},
            {'parameter_id': 8, 'lower_limit': 0, 'upper_limit': 66.5},
            {'parameter_id': 9, 'lower_limit': 0, 'upper_limit': 4.75},
            {'parameter_id': 10, 'lower_limit': -42, 'upper_limit': 122}
        ]

        # Loop through each row in the process events DataFrame
        for index, row in process_events_df.iterrows():
            station_id = row['station_id']
            # Assuming 'id' column represents the event ID
            event_id = row['id']
            # Assuming 'end_time' is the correct column for the event creation time
            created_at = row['end_time']

            # Determine parameter range based on station ID
            if station_id == 1:
                parameter_range = range(1, 5)
            elif station_id == 2:
                parameter_range = range(5, 8)
            elif station_id == 3:
                parameter_range = range(8, 10)
            elif station_id == 4:
                parameter_range = [10]
            else:
                continue  # Skip if station ID is invalid

            # Generate results for each parameter in the determined range
            for parameter_id in parameter_range:
                # Adjust index to match list indexing
                parameter_data = parameters_data[parameter_id - 1]
                lower_limit = next(
                    limit['lower_limit'] for limit in limits_data if limit['parameter_id'] == parameter_id)
                upper_limit = next(
                    limit['upper_limit'] for limit in limits_data if limit['parameter_id'] == parameter_id)

                # Calculate midpoint of the limits range
                midpoint = (lower_limit + upper_limit) / 2

                # Generate result with variation around the midpoint using normal distribution
                # Adjust scale depending on the range of limits
                scale = (upper_limit - lower_limit) / \
                    20  # Adjust this factor as needed
                value = np.random.normal(midpoint, scale)

                # Ensure generated value is within limits range
                value = max(lower_limit, min(upper_limit, value))

                result = {
                    "event_id": event_id,
                    "parameter_id": parameter_id,
                    "value": value,
                    "created_at": created_at
                }
                results.append(result)

        return results
    # TODO remove, used for temp inserts

    def replace_results_table(self, new_results):
        try:

            # Create a new results table using the same schema
            create_query = """
                CREATE TABLE results (
                    -- Define columns based on your schema
                    id SERIAL PRIMARY KEY,
                    event_id INT,
                    parameter_id INT,
                    value FLOAT,
                    created_at TIMESTAMP
                )
            """
            self.client.execute_query(create_query)

            # Convert new_results to DataFrame
            new_results_df = pd.DataFrame(new_results)

            # Insert new records into the new results table
            new_results_df.to_sql(
                'results', self.client.engine, if_exists='append', index=False)

            # Commit the changes
            self.client.session.commit()

            print("Results table replaced successfully!")
        except Exception as e:
            print(f"Error replacing results table: {e}")
    # TODO remove, used for temp inserts

    def modify(self):
        df = self.client.execute_query(self.query_master.get_results())
        # Initialize variables
        event_id = 1

        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            # Assign the current event_id to the row
            df.at[index, 'event_id'] = event_id
            # Update event_id according to the rules
            if row['parameter_id'] == 4:
                event_id += 1
            elif row['parameter_id'] == 7:
                event_id += 1
            elif row['parameter_id'] == 9:
                event_id += 1
            elif row['parameter_id'] == 10:
                event_id += 1

        self.client.execute_query_t(df, update=True, batch_size=1000)
