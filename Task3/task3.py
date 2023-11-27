from Task3.create_indexing import create_index, check_index_performance
from Task3.create_caching import get_data_with_caching, check_data_insertion_random_sample
import time


if __name__ =="__main__":

    #PART 3 OPTIMIZATION
    #Indexing
    create_index('Supplier', 'SupplierName')
    create_index('Inventory', 'Quantity')
    create_index('OrderDetails', 'OrderID')
    check_index_performance('OrderDetails', 'OrderID', '178')

    #Caching
    order_id = 178
    query = "SELECT * FROM OrderDetails WHERE OrderID = %s"
    start_time = time.time()
    data = get_data_with_caching(query, (order_id,))
    end_time = time.time()
    print(f"Data: {data}")
    print(f"Time taken for the first call: {end_time - start_time} seconds")

    # Timing the second call (cached)
    start_time = time.time()
    data = get_data_with_caching(query, (order_id,))
    end_time = time.time()
    print(f"Data: {data}")
    print(f"Time taken for the second call: {end_time - start_time} seconds")

    # Call the function to check data insertion with random samples -> Proof
    check_data_insertion_random_sample()

    pass