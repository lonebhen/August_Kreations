from twilio.rest import Client


def send_message(product_name,name,phone_number,location,city,quantity):
    account_sid = 'AC1bd906b90655afdf63d8012d6a0e691b' 
    auth_token = 'd3ac59848c3695024e40929afe6ea887'
    client = Client(account_sid, auth_token)


    message = client.messages \
                .create(
                     body="{} wants to buy {} in a quantity of {} located in {} in the city {} reach out on {}".format(name,product_name,quantity,location,city,phone_number),
                     from_='+15673444515',
                     to='+233544055730'
                 )
    
    # print(message)