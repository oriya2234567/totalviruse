import requests
import os
import time
import sys
my_api_key = "f651578a5c868d30176821d0b261506ef968969f2a7260df9ebbe2808bbf6fc0"
url_of_post_file =  r"https://www.virustotal.com/vtapi/v2/file/scan"
url = r'https://www.virustotal.com/vtapi/v2/file/report'
def id_virus_api_wait_for_the_report(id):
        time.sleep(35)
        params = {'apikey': my_api_key, 'resource': id }
        print(id)
        response3 = requests.get(url, params=params)
        # print(response3.status_code)
        
            # print(response3.json())
        response3 = response3.json()
        if response3["positives"] > 0:
                 print("have virus in the foler")
                 sys.exit()
                 
       

        



def get_file_to_virus_api(file_path):
    params = {"apikey": my_api_key}
    file_to_binari ={
        "file" : open(file_path,"rb") 
                } 
    
   
    print("i send" ,file_path)
    response = requests.post(url_of_post_file, files = file_to_binari, params=params)
    print(response.json())
    file_to_binari["file"].close()
    res = response.json()
    

    id_virus_api_wait_for_the_report(res["scan_id"])
    

   


def open_every_file_in_dir(file_path):
    
    for item in os.listdir(file_path):
        if os.path.isdir(file_path+"//"+item) is not True :
            get_file_to_virus_api(file_path +"//"+item)
            print(file_path +"//"+item)
            
        else:
            open_every_file_in_dir(file_path+"//"+item)


def main():
# print(os.listdir(r"C://Users//User//OneDrive//שולחן העבודה//theviruse"))
    open_every_file_in_dir(r"C://Users//User//OneDrive//שולחן העבודה//theviruse")


if __name__ == "__main__":
    main()




