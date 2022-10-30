## installation :

1) ```bash
   wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
   ```

2) ```bash
   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
   ```

3) ```bash
   sudo apt-get update
   ```

4) ```bash
   sudo apt-get install -y mongodb-org
   ```

## start mongodb :

* in terminal tab :

1) ```bash
   sudo mongod
   ```

* in another tab : (don't close the last tab)

2) ```bash
   sudo systemctl start mongod
   ```

3) ```bash
   sudo systemctl status mongod
   # or
   sudo service mongod status
   ```

4) ```bash
   sudo systemctl enable mongod
   ```

5) ```bash
   mongosh
   ```

## stop mongodb :

```bash
sudo systemctl stop mongod
```

## restart mongodb :

```bash
sudo systemctl restart mongod
```

-----------------------

## commands :

### notes :

* mongodb can connect database in two ways :
  1) by using db you but it before in mongodb server (use the link to connect it)
  2) by using local connection : mongodb://localhost:27017

* table => collection
* column => field
* row => document (document may have sub documents) (it is remarked as { })

```scala
show dbs // to show available databases
db // prints the current database
```

```scala
use blog // create database blog
```

```scala
db.createCollection('users'); // create table users
```

```scala
show collections; // show tables of current DB
```

```scala
db.users.drop(); // drop users table
```

```scala
db.runCommand( { hello: 1 } ) # to run command 
db.adminCommand( { hello: 1 } ) # to run command as admin
```

```scala
load("myScript.js") // run js file
```

### insert :

```scala
db.users.insertOne({name: "Max"}) // if table users not found , will be created
db.users.insert([{name: "Max"}, {name:"Alex"}]) // ordered bulk insert (we added two documents (objects or rows))
db.users.insert([{name: "Max"}, {name:"Alex"}], {ordered: false}) // unordered bulk insert
db.users.insertMany([{name: "Max"}, {name:"Alex"}]) //insertMany is the same as insert 
db.users.insert({date: ISODate()})//2022-07-28T16:43:28.135+00:00
db.users.insert({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}}) // we can add sub document in document
```

### filter :

```scala
db.users.findOne() // gets first document in users table
db.users.find() // gets documents of users table if found
db.coll.find().pretty() 
db.users.find({"name" : "ahmed"})
db.users.find({date: ISODate("2020-09-25T13:57:17.180Z")})
db.users.find({"name" : "ahmed"}).limit(2) // get only first 2 documents of the filter result
```

### count :

```scala
db.users.find().count() // gets the number of documents in users table.
db.users.find({"name" : "ahmed"}).count()
```

### sort :

```scala
// 1 ==> asc
// -1 ==> Descend
db.users.find({"name" : "ahmed"}).sort({name : 1})//sort by name asc 
db.users.find({"name" : "ahmed"}).sort({name : -1}) //sort by name Descend
```

### distinct :

```scala
db.users.distinct("name") // get all values in the field name 
//[ 'Alex', 'Max', 'ahmed', 'ahmedissa' ]
```

### comparison :

```scala
db.coll.find({"year": {$gt: 1970}}) // greater than
db.coll.find({"year": {$gte: 1970}}) // greater than or equal
db.coll.find({"year": {$lt: 1970}}) // less than
db.coll.find({"year": {$lte: 1970}})
db.coll.find({"year": {$ne: 1970}}) 
db.coll.find({"year": {$in: [1958, 1959]}}) //1958 or 1959
db.coll.find({"year": {$nin: [1958, 1959]}})
```

### logical :

```scala
db.coll.find({name:{$not: {$eq: "Max"}}})
db.coll.find({$or: [{"year" : 1958}, {"year" : 1959}]})
db.coll.find({$nor: [{price: 1.99}, {sale: true}]})
db.coll.find({
  $and: [
    {$or: [{qty: {$lt :10}}, {qty :{$gt: 50}}]},
    {$or: [{sale: true}, {price: {$lt: 5 }}]}
  ]
})
```

### update :

```scala
db.coll.update({"_id": 1}, {"year": 2016}) // WARNING! Replaces the entire document
db.coll.update({"_id": 1}, {$set: {"year": 2016, name: "Max"}})
db.coll.update({"_id": 1}, {$unset: {"year": 1}})
db.coll.update({"_id": 1}, {$rename: {"year": "date"} })
```

### delete :

```scala
// remove is same of delete 
// we can use deleteOne , deleteMany
db.coll.remove({name: "Max"})
db.coll.remove({name: "Max"}, {justOne: true})
db.coll.remove({}) // WARNING! Deletes all the docs but not the collection itself and its index definitions
db.coll.remove({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
db.coll.findOneAndDelete({"name": "Max"})
```

### drop :

```scala
db.coll.drop()    // removes the collection and its index definitions
db.dropDatabase() // double check that you are *NOT* on the PROD cluster... :-)
```

### collection functions :

```scala
db.coll.stats()
db.coll.storageSize()
db.coll.totalIndexSize()
db.coll.totalSize()
db.coll.validate({full: true})
db.coll.renameCollection("new_coll", true) // 2nd parameter to drop the target collection if exists
```

### mongo DB cheat sheet :

https://www.mongodb.com/developer/products/mongodb/cheat-sheet/