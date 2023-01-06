
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

7) git push origin master         **note** origin is is remote name(origin is the remote ame for git hub ,there is also a name for git lab and others) , master is branch name

-----

## adding an existing project to git hub :

1) get in project folder 
2) git init
3) git add . 
4) git commit -m "any message"
5) make a new repo in github (or go to an aready exist one )
6) git add README.md  
8) git branch -M main
8) git remote add origin https://github.com/Ahmed3117/test2.git 
9) git push -u origin main    (-u means pull first befor push , because if this repo you wanted to connect it => https://github.com/Ahmed3117/test2.git was aready used by another contributer then it already has files on it ,so you have to pull these files before you push yours)
**number 9 => git push -u origin main  => we can do it into two steps :
		git pull
		git push

-----------------

### notes:

* #### get changes status:

  git status

* #### get my branches:

  git branch

* #### get the current remote :

  git remote -v

* #### to remove a file from the stage:

  git reset head file_name
* #### show all commits you did in the current branch :
	git log  (هيديك كل الكوميتس اللى اتعملت وامتى ويديك اى دى لكل واحده)
* #### to undo a commit :
	git checkout commit_id   (you can get commit_id from this command => git log  )
* #### create new branch :
	git checkout -b branch_name
* #### switch to another branch:
	git checkout  branch_name
* #### to push in a new branch:

  git checkout  branch_name
  
  git add .
  
  git commit -m"any message"
  
  git push --set-upstream origin branch_name
* #### unstage file from stage (stage made by => git add .)
	git restore --staged file_name
	or all
	git restore --staged * 
	
* #### save some files in staging area and keep them not committed untill you can reset them later to keep working of them :
	* git add .  (or add some files to the staging area)
	* git stash (hide these files on the staging area from commit stage)
		*you can give message to the stash as acomment : *

		git stash save "your comment"
		
	* git status (it will say nothing to commit => because files in staging area not seen to him)
	* git stash list (show the list of stashes => we now have only one stash)
		*this will give a list of stashes every one with number like this :
		stash@{0}
		stash@{1}
		stash@{2}*
	* go work as you want in the project and make commits and push if you want 
	* now we need these files in the stash to get them back to the project to work on them:
		git stash pop  (will retrieve the last stash to the project and delete it from stashes)
		or 
		git stash apply  (will retrieve the last stash to the project but keep it in stashes so you can use it again later)
		*we can pop or apply stash by its number like this :
		git stash pop stash@{1}*
	* remove stash 
		git drop   => remove last stash and its content
		git stash clear => remove all stashes
#### revert a commit : 
i need my current code in vscode to be the code of the last commit or any previous commit :
the head points to the last commit and this means that the last commit is the current active commit . so we need to change the head pointer to another commit :
	git reset --hard HEAD~1   ---> point to the last commit 
#### reset commits :
##### the problem :
	you made many commits and pushed them to the origin but you need to remove last commit or more 
##### solution :
	* git log  => to get commits ids
	* git reset --hard commit_id  (the last commit you need to keep (you need to stop on it so all commits after it will be removed))
	* git push origin main --force  => to update the origin with the commit we stopped on it
#### gitignore :
 create file with name =>   .gitignore     then put files or directories you want to be untracked by git  like this :
 ```.gitignore

*.log    => all files with extention .log
!vip.log  => except this file
migrations/ => the folder with this name
text.txt  => the file with name

```
#### force add files even if they are ignored in .gitignore file :
	git add -f text.txt

------

## branching
#### get my branches:
  git branch
#### create new branch :
	git branch branch_name
#### switch to another branch:
	git checkout branch_name
#### create new branch and switch to it directly :
	git checkout -b branch_name
#### delete branch
	git branch -d branch_name  (will refuse to delete it if there are some changed not merged to the main)
#### force delete branch
	git branch -D branch_name
#### rename branch
	* go to the branch => git checkout branch_name
	* rename it => git branch -m new_name
#### merge branch to the master
	* go to the master branch => git checkout master
	* merge the branch to the master => git merge branch_name
-------------------------------------
### work in team  first way (merge in local then push)
* the main project is on master branch
* to make your changes create another branch to work on it :
		1) git checkout -b new_branch_name
		2) git add .
		3) git commit -m"any message"
* now you need to merge your changes in your branch with the changes in the master :
		5) git checkout -b master  => back to the master branch
		6) git merge new_branch_name  
* now you can push changes in the master to the origin in github
	7) git push origin master


### work in team  second way (push changes from the branch to this branch in origin then make pull request to the main)
* the main project is on master branch
* to make your changes create another branch to work on it :
		1) git checkout -b new_branch_name
		2) git add .
		3) git commit -m"any message"
* now push changes in this branch to the origin in github :
		5) git push origin new_branch_name 
		*once this command is executed , the changes in this branch will be pushed to the origin and wait for you to send pull request to the main *
* now you can push changes in the master to the origin in github
	7) git push origin master
----------------------------------------------------------
## invite a collaborator:

   * go to your repo

   * settings

   * manage access

   * invite a collaborator

   * write a collaborator email in github

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
الزيرو الفيديو رقم 8

* if you used public key (ssh) , you will use ssh instead of https while cloning a repo or other places.
------------------
## alias :
بنحتاجه علشان نختصر الاوامر
Ex => git config --global alias.st status  (now we can say git st  instead of git status)
 كلمة جلوبال لو محططهاش هيعمل الاياس ده على مستوى الريبو الحالية فقط
Ex => git config --global alias.cm "commit -m"   (we but the command in " " because it is more than a word)
(now we can say => git cm "a new commit"  instead of => git commit -m " a new commit")