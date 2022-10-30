user name: ahmedprog
email : ahmedissaprog@gmail.com
password : githubPASSWORD010*#

token: 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

---------------

user name: Ahmed3117
email : ahmedibra3117@gmail.com
password : withALLAH010*#

token: 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

			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

**************************
![](/home/ahmedissa/Pictures/git.png)

## building a repo and project :

1) create a new repo from git hub with read me file

2) go to folder you need to clone the repo on it

3) git clone https://github.com/Ahmed3117/test.git

4) work as you want in your project

5) add changes to the stage :

   * to add all changes in one time :

     git add .

   * to add changes of just one file :

     git add file_name (or file path)

   * to add changes of more than a file :

     git add first_file second_file third_file ( just let a space between files)

6) git commit -m "any message"      (to move files from stage  to local repo)

7) git push origin master         **note** origin is is remote name , master is branch name

### notes:

* get changes status:

  git status

* get my branches:

  git branch

* get the current remote :

  git remote -v

* to remove a file from the stage:

  git reset head file_name
  
* to push in a new branch:

  git checkout -b lecture3
  
  git add .
  
  git commit -m"any message"
  
  git push --set-upstream origin lecture3

----------------------------------------------------------
## adding an existing project to git hub :

1) get in project folder 
2) git init
3) git add . 
4) git commit -m "any message"
5) make a new repo in github
6) git add README.md  
8) git branch -M main
8) git remote add origin https://github.com/Ahmed3117/test2.git 
9) git push -u origin main
----------------------------------------------------------
## invite a collaborator:

   * go to your repo

   * settings

   * manage access

   * invite a collaborator

   * write a collaborator name in github

   * now you sent him an invitation if he accepted it he can shre this repo with you and can modify on it as permissions control

   * any one of collaborators make changes the other one should pull them

        git pull origin

------------------------

## configurations: 

#### (like username , password , color of added files or untracked files or ... ,......)

1) to get what configurations you have a permission to change them :
    git config --list     or   git config -l
2) to get all available configurations :
    git help config
3) changing on configs:
    * get a config value:
        git config --global user.email    ===> it gets current users email
    * modifying a config:
        git config --global user.email "ahmed@gmail.com"  ===> user email changed
    * removing a config:
        git config --global --unset user.name
4) to modify configs using editor :
    git config --global --edit
    to understand this well , go to vedio number 7 in elzero (the last 3 miniuts in the vedeo)

-------------

## public eky:

بيستخدم علشان مش كل مرة تدخل يسألك على الاسم والباسورد

