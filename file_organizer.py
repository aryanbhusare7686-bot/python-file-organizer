from pathlib import Path 
#Generate a unique file name if file already exists 
def get_unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_destination = destination.parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1
def organize_files():
#organize files from Downloads folder 
    folder = Path.home()/ "Downloads"
    images = folder/ "Images"
    documents = folder / "Documents"
    others = folder /"Others"
    print("-----Starting File Organizer-----")
    #check each file and move to appropriate folder
    for item in folder.iterdir():
        if item.is_file():
            if item.suffix.lower() in [".jpg" , ".jpeg" , ".png"]:
                destination = images/item.name 
                destination = get_unique_destination(destination)
                try: 
                    item.rename(destination)
                    print(item.name , "-> moved to images")
                except Exception as e : 
                    print("Error: ", item.name, "->" , e)
                  
            elif item.suffix.lower() in [".pdf" , ".txt" , ".docx"]:
                destination = documents/item.name 
                destination = get_unique_destination(destination)
                try:
                    item.rename(destination)
                    print(item.name , "-> moved to documents")
                except Exception as e : 
                    print("Error: ", item.name , "-> " , e )
            else:
                destination = others / item.name
                destination = get_unique_destination(destination)
                try :
                    item.rename(destination)
                    print(item.name, "-> moved to others")
                except Exception as e : 
                                    print("Error: ", item.name , "-> " , e )
    print("-----File organization completed-----")
organize_files()
