#Question-02: Sports tournament record maintenance. Python program to perfrom following operations after creating a dictionary representing the current points of teams in tournament:
#add_team
#remove_team
#update_points
#get_top_n_teams
#write_to_file


class Sports:
    def __init__(self):
        self.teams={}
        
    def add_team(self,name,points):
        if name not in self.teams:
            self.teams[name]=points
            print(f"Team '{name}'added successfully!")
        else:
            print(f"Team '{name}' already exists!")
            
        
    def remove_team(self,name):
        if name in self.teams:
            del self.teams[name]
            print(f"Team '{name}' deleted successfully!")
        else:
            print(f"Team '{name}' does not exist!")
            
    def update_points(self,name,new_points):
        if name in self.teams:
            self.teams[name]+=new_points
            print(f"Team '{name}' updated successfully!")
        else:
            print(f"Team '{name}' does not exist!")
        
    def get_top_n_teams(self,n):
        sorted_teams=sorted(self.teams.items(), key=lambda x: x[1], reverse=True)
        print(f"The top {n} teams are: {sorted_teams[:n]}")    
    
    def write_to_file(self,filename):
        with open(filename,'w') as f:
            for x,y in self.teams.items():
                f.write(f"{x}: {y}\n")
        x=open(filename)
        print(x.read())
        
    
myteam=Sports()

while True:
    
    print("Operations: ")
    print("1. Add team")
    print("2. Remove team")
    print("3. Update points")
    print("4. Get top n teams")
    print("5. Write to file")
    print("6. Exit")
    
    choice=int(input("Enter choice: "))
    
    if choice==1:
        value=int(input("Enter no. of teams you want to add: "))
        for x in range(1,value+1):
            name=input("Enter team name: ")
            value=int(input("Enter team points: "))
            myteam.add_team(name,value)
        print("The dictionary is: ",myteam.teams)
    
    elif choice==2:
        name=input("Enter name of team: ")
        myteam.remove_team(name)
        
    elif choice==3:
        name=input("Enter team name: ")
        new_value=int(input("Enter new team points: "))
        myteam.update_points(name,new_value)
        
    elif choice==4:
        n=int(input("Enter number of tops teams you want: "))
        myteam.get_top_n_teams(n)
        
    elif choice==5:
        filename=input("Enter file name: ")
        myteam.write_to_file(filename)
        
    elif choice==6:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice.Please choose again!")
        
            
            
    