

from storage import save_contact,load_contact
def add_contact(name,mobile,email,address):

    details = load_contact()

    detail = {

        'name' : name,
        'mobile' : mobile,
        'email' : email,
        'address' : address,
    }
    details.append(detail)
    save_contact(details)

def view_contact():
    details = load_contact()
    print("\n Details: \n")
    for i, detail in enumerate(details, start=1):
        print(f"{i}.Nmae: {detail['name']},Mobile: {detail['mobile']},Email:{detail['email']},Address: {detail['address']}")
def remove_contact(index):
    details = load_contact()
    if 0<index=len(details):
        del details[index-1]
        save_contact(details)
    else:
        print("invalid index")
def search_contact(query):
    details = load_contact()
    result = []
    for detail in details:
        if query == detail['mobile']:
            result.append(detail)
    print("\n search result: \n")
    for i, detail in enumerate(result, start=1):
        print(
            f"{i}.Nmae: {detail['name']},Mobile: {detail['mobile']},Email:{detail['email']},Address: {detail['address']}")
