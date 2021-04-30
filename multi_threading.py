# Function which is get data from another 3 functions
def dashboard_data_thread1(user):
    
    ctx = {}

    # get data from data_1, data_2, data_3 functions

    data1 = data_1(user)
    data2 = data_2(user)
    data3 = data_3(user)

    # data 1
    ctx['orders_count'] = data1['orders_count']
    ctx['total_orders'] = data1['total_orders']
   

    # data 2
    ctx['return_orders'] = data2['return_orders']
    ctx['logistics_orders'] = data2['logistics_orders']
   

    # data3
    ctx['seller_amount'] = data3['seller_amount']
    ctx["over_dues_total"] = data3["over_dues_total"]
    
    return ctx

# Function which is get data from another 3 functions
def dashboard_data_thread2(user):

    ctx = {}
    
     # get data from data_4, data_5, data_6 functions

    data4 = data_4(user)
    data5 = data_5(user)
    data6 = data_6(user)

    # data 4
    ctx['product_category'] = data4['product_category']
    ctx['submitted_products'] = data4['submitted_products']
   

    # data 5
    ctx['total_repayment_amount'] = data5['total_repayment_amount']
    ctx['total_credit'] = data5['total_credit']
 

    # data6
    ctx['net_pay'] = data6['net_pay']
    ctx["total"] = data6["total"]
  
    return ctx

import threading
from queue import Queue

def create_dashboard_data_request(request):
    user = request.user
    new_dict = {}

    threads_list = []
    que = Queue()

    # create thread objects
    t1 = threading.Thread(target=lambda q, arg1: q.put(dashboard_data_thread1(arg1)), args=(que, user), name="t1")
    t2 = threading.Thread(target=lambda q, arg1: q.put(dashboard_data_thread2(arg1)), args=(que, user), name="t1")

    # start thread
    t1.start()
    t2.start()

    #end thread
    threads_list.extend([t1, t2])
    for t in threads_list:
        t.join()

    # get return data from the function called by using thread
    while not que.empty():
        result = que.get()
        new_dict.update(result)
    print(new_dict)

   
    return HttpResponse("ok")
