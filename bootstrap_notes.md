## screan sizes:

* lg >= 1200 px
* md >= 992 px
* sm >=768 px
* xs <= 768 px

## classes notes:

### grid classes:

* col-lg-offset-2   ==> in case of large size (lg) ,ignore the second grid cell 
* col-lg-push-3  ==> in case of large size (lg) , move three grids forward 
* col-lg-pull-3  ==> in case of large size (lg) , move three grids backward

### visable&hidden:

* visible-lg ==> to be visible in large screen but in md or sm or sx it will disappear

* hidden-lg ==> hidden in all 

  Ex:

  ```html
  <div class="visible-lg"></div>
  ```

  Ex:

  ```html
  <div class="visible-lg-inline"></div>  
  # it will appear as inline in large screen
  ```

  

## clearfix:

used to isolate one (or more) of grids from others 

```html
<div class="clearfix">...</div>
```

## circular image:

* image:

  ![](/home/ahmedissa/Pictures/circularimage.png)

* html:

  ```html
  <img id="img" class="nav_img" alt="" height="32" width="32" src="img/ahmed.png">
  ```

  

* css:

  ```css
  .nav_img{
      border-radius: 50%;
  }
  ```


## control image fluid :

* html:

  ```html
  <div class="container">
          <img class="img-fluid home_img" src="img/eng1.jpg" alt="">
  </div>
  ```

  

* css:

  ```css
  img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 50%;
  }
  ```

  

## search & menue:

- image:

![](/home/ahmedissa/Pictures/searchmenue.png)

* html:

```html

<div class="dropdown-menu dropdown-menu-dark border-0 pt-0 mx-0 rounded-3 shadow overflow-hidden" style="width: 280px;">
    <form class="p-2 mb-2 bg-dark border-bottom border-dark">
      <input type="search" class="form-control form-control-dark" autocomplete="false" placeholder="Type to filter...">
    </form>
    <ul class="list-unstyled mb-0">
      <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#">
        <span class="d-inline-block bg-success rounded-circle" style="width: .5em; height: .5em;"></span>
        Action
      </a></li>
      <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#">
        <span class="d-inline-block bg-primary rounded-circle" style="width: .5em; height: .5em;"></span>
        Another action
      </a></li>
      <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#">
        <span class="d-inline-block bg-danger rounded-circle" style="width: .5em; height: .5em;"></span>
        Something else here
      </a></li>
      <li><a class="dropdown-item d-flex align-items-center gap-2 py-2" href="#">
        <span class="d-inline-block bg-info rounded-circle" style="width: .5em; height: .5em;"></span>
        Separated link
      </a></li>
    </ul>
  </div>
```

* css:

```css
.dropdown-menu {
    position: static;
    display: block;
    width: auto;
    margin: 4rem auto;
}
```

## footer:

bootstrap footers :

https://mdbootstrap.com/docs/standard/navigation/footer/

### ex:

* image:

![](/home/ahmedissa/Pictures/footer.png)

* html:

```html
 
  <!-- Footer -->
      <section id="footer">
          <div class="container">
              <div class="row text-center text-xs-center text-sm-left text-md-center">
                  <div class="col-xs-12 col-sm-4 col-md-4">
                      <h5>Quick links</h5>
                      <ul class="list-unstyled quick-links">
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>Home</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>About</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>FAQ</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>Get Started</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>Videos</a></li>
                      </ul>
                  </div>
                  <div class="col-xs-12 col-sm-4 col-md-4">
                      <h5>Quick links</h5>
                      <ul class="list-unstyled quick-links">
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>Home</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>About</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>FAQ</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>Get Started</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>Videos</a></li>
                      </ul>
                  </div>
                  <div class="col-xs-12 col-sm-4 col-md-4">
                      <h5>Quick links</h5>
                      <ul class="list-unstyled quick-links">
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>Home</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>About</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>FAQ</a></li>
                          <li><a href="https://www.fiverr.com/share/qb8D02"><i class="fa fa-angle-double-right"></i>Get Started</a></li>
                          <li><a href="https://wwwe.sunlimetech.com" title="Design and developed by"><i class="fa fa-angle-double-right"></i>Imprint</a></li>
                      </ul>
                  </div>
              </div>
              <div class="row">
                  <div class="col-xs-12 col-sm-12 col-md-12 mt-2 mt-sm-5">
                    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
                    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
                    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
                    
                    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
                    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet" integrity="sha256-MfvZlkHCEqatNoGiOXveE8FIwMzZg4W85qfrfIFBfYc= sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">
                   
                    <div class="container social_margin">
                        <div class="text-center center-block">
                            <a href="https://www.facebook.com/bootsnipp"><i id="social-fb" class="fa fa-facebook-square fa-3x social"></i></a>
                            <a href="https://twitter.com/bootsnipp"><i id="social-tw" class="fa fa-twitter-square fa-3x social"></i></a>
                            <a href="https://plus.google.com/+Bootsnipp-page"><i id="social-gp" class="fa fa-google-plus-square fa-3x social"></i></a>
                            <a href="mailto:bootsnipp@gmail.com"><i id="social-em" class="fa fa-envelope-square fa-3x social"></i></a>
                        </div>
                    </div>                          
                    <div class="container">
                  </div>
                 
              </div>	
              <div class="row">
                  <div class="col-xs-12 col-sm-12 col-md-12 mt-2 mt-sm-2 text-center text-white">
                      <p><u><a href="https://www.nationaltransaction.com/">National Transaction Corporation</a></u> is a Registered MSP/ISO of Elavon, Inc. Georgia [a wholly owned subsidiary of U.S. Bancorp, Minneapolis, MN]</p>
                      <p class="h6">© All right Reversed.<a class="text-green ml-2" href="https://www.sunlimetech.com" target="_blank">Sunlimetech</a></p>
                  </div>
                 
              </div>	
          </div>
      </section>
      <!-- ./Footer -->
```

* css:

```css

/* Footer */
@import url('https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css');
section {
    padding: 60px 0;
}

section .section-title {
    text-align: center;
    color: #007b5e;
    margin-bottom: 50px;
    text-transform: uppercase;
}
#footer {
    background: #007b5e !important;
}
#footer h5{
	padding-left: 10px;
    border-left: 3px solid #eeeeee;
    padding-bottom: 6px;
    margin-bottom: 20px;
    color:#ffffff;
}
#footer a {
    color: #ffffff;
    text-decoration: none !important;
    background-color: transparent;
    -webkit-text-decoration-skip: objects;
}
#footer ul.social li{
	padding: 3px 0;
}
#footer ul.social li a i {
    margin-right: 5px;
	font-size:25px;
	-webkit-transition: .5s all ease;
	-moz-transition: .5s all ease;
	transition: .5s all ease;
}
#footer ul.social li:hover a i {
	font-size:30px;
	margin-top:-10px;
}
#footer ul.social li a,
#footer ul.quick-links li a{
	color:#ffffff;
}
#footer ul.social li a:hover{
	color:#eeeeee;
}
#footer ul.quick-links li{
	padding: 3px 0;
	-webkit-transition: .5s all ease;
	-moz-transition: .5s all ease;
	transition: .5s all ease;
}
#footer ul.quick-links li:hover{
	padding: 3px 0;
	margin-left:5px;
	font-weight:700;
}
#footer ul.quick-links li a i{
	margin-right: 5px;
}
#footer ul.quick-links li:hover a i {
    font-weight: 700;
}

@media (max-width:767px){
	#footer h5 {
    padding-left: 0;
    border-left: transparent;
    padding-bottom: 0px;
    margin-bottom: 10px;
}
}

```

## icon:

html :

```html
<!-- call this befor body -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.6.0/font/bootstrap-icons.css">

<!-- this example to icon in button -->
<button class="btn btn-outline-info" type="submit">
    <i class="bi bi-arrow-left-circle-fill"></i>Back</button>

```

## image fill a div:

html :

```html
<div class="container-fluid">
    <img class="img-change" src="" alt="">
</div>
```

css :

```css
.img-change{
    width: 100%;
    object-fit: cover;
    height: 38vw;
    }
```

-------------

Table :

  <table class="table">
    <thead>
      <tr>
        <th>Name</th>
        <th>E-mail</th>
        <th>Title</th>
        <th>Department</th>
        <th>Status</th>
        <th>Position</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John Doe</td>
        <td>john.doe@gmail.com</td>
        <td>Software engineer</td>
        <td>IT department</td>
        <td>Active</td>
        <td>Senior</td>
        <td>
          <button type="button" class="btn btn-primary btn-sm">
            Edit
          </button>
        </td>
      </tr>
      <tr>
        <td>Alex Ray</td>
        <td>alex.ray@gmail.com</td>
        <td>Consultant</td>
        <td>Finance</td>
        <td>Onboarding</td>
        <td>Junior</td>
        <td>
          <button type="button" class="btn btn-primary btn-sm">
            Edit
          </button>
        </td>
      </tr>
      <tr>
        <td>Kate Hunington</td>
        <td>kate.hunington@gmail.com</td>
        <td>Designer</td>
        <td>UI/UX</td>
        <td>Awaiting</td>
        <td>Senior</td>
        <td>
          <button type="button" class="btn btn-primary btn-sm">
            Edit
          </button>
        </td>
      </tr>
    </tbody>
  </table>
html :

```html
<div class="container my-5">

  <table class="table">
    <thead>
      <tr>
        <th>Name</th>
        <th>E-mail</th>
        <th>Title</th>
        <th>Department</th>
        <th>Status</th>
        <th>Position</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John Doe</td>
        <td>john.doe@gmail.com</td>
        <td>Software engineer</td>
        <td>IT department</td>
        <td>Active</td>
        <td>Senior</td>
        <td>
          <button type="button" class="btn btn-primary btn-sm">
            Edit
          </button>
        </td>
      </tr>
      <tr>
        <td>Alex Ray</td>
        <td>alex.ray@gmail.com</td>
        <td>Consultant</td>
        <td>Finance</td>
        <td>Onboarding</td>
        <td>Junior</td>
        <td>
          <button type="button" class="btn btn-primary btn-sm">
            Edit
          </button>
        </td>
      </tr>
      <tr>
        <td>Kate Hunington</td>
        <td>kate.hunington@gmail.com</td>
        <td>Designer</td>
        <td>UI/UX</td>
        <td>Awaiting</td>
        <td>Senior</td>
        <td>
          <button type="button" class="btn btn-primary btn-sm">
            Edit
          </button>
        </td>
      </tr>
    </tbody>
  </table>

</div>
```

Another Table :

  <div class="shadow-4 rounded-5 overflow-hidden">
    <table class="table align-middle mb-0 bg-white">
      <thead class="bg-light">
        <tr>
          <th>Name</th>
          <th>Title</th>
          <th>Status</th>
          <th>Position</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <div class="d-flex align-items-center">
              <img
                   src="https://mdbootstrap.com/img/new/avatars/8.jpg"
                   alt=""
                   style="width: 45px; height: 45px"
                   class="rounded-circle"
                   />
              <div class="ms-3">
                <p class="fw-bold mb-1">John Doe</p>
                <p class="text-muted mb-0">john.doe@gmail.com</p>
              </div>
            </div>
          </td>
          <td>
            <p class="fw-bold mb-1">Software engineer</p>
            <p class="text-muted mb-0">IT department</p>
          </td>
          <td>
            <span class="badge badge-success rounded-pill">Active</span>
          </td>
          <td>Senior</td>
          <td>
            <button type="button" class="btn btn-link btn-sm btn-rounded">
              Edit
            </button>
          </td>
        </tr>
        <tr>
          <td>
            <div class="d-flex align-items-center">
              <img
                   src="https://mdbootstrap.com/img/new/avatars/6.jpg"
                   class="rounded-circle"
                   alt=""
                   style="width: 45px; height: 45px"
                   />
              <div class="ms-3">
                <p class="fw-bold mb-1">Alex Ray</p>
                <p class="text-muted mb-0">alex.ray@gmail.com</p>
              </div>
            </div>
          </td>
          <td>
            <p class="fw-normal mb-1">Consultant</p>
            <p class="text-muted mb-0">Finance</p>
          </td>
          <td>
            <span class="badge badge-primary rounded-pill">Onboarding</span>
          </td>
          <td>Junior</td>
          <td>
            <button
                    type="button"
                    class="btn btn-link btn-rounded btn-sm fw-bold"
                    data-mdb-ripple-color="dark"
                    >
              Edit
            </button>
          </td>
        </tr>
        <tr>
          <td>
            <div class="d-flex align-items-center">
              <img
                   src="https://mdbootstrap.com/img/new/avatars/7.jpg"
                   class="rounded-circle"
                   alt=""
                   style="width: 45px; height: 45px"
                   />
              <div class="ms-3">
                <p class="fw-bold mb-1">Kate Hunington</p>
                <p class="text-muted mb-0">kate.hunington@gmail.com</p>
              </div>
            </div>
          </td>
          <td>
            <p class="fw-normal mb-1">Designer</p>
            <p class="text-muted mb-0">UI/UX</p>
          </td>
          <td>
            <span class="badge badge-warning rounded-pill">Awaiting</span>
          </td>
          <td>Senior</td>
          <td>
            <button
                    type="button"
                    class="btn btn-link btn-rounded btn-sm fw-bold"
                    data-mdb-ripple-color="dark"
                    >
              Edit
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
html :

```html
<div class="container my-5">
  <div class="shadow-4 rounded-5 overflow-hidden">
    <table class="table align-middle mb-0 bg-white">
      <thead class="bg-light">
        <tr>
          <th>Name</th>
          <th>Title</th>
          <th>Status</th>
          <th>Position</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <div class="d-flex align-items-center">
              <img
                   src="https://mdbootstrap.com/img/new/avatars/8.jpg"
                   alt=""
                   style="width: 45px; height: 45px"
                   class="rounded-circle"
                   />
              <div class="ms-3">
                <p class="fw-bold mb-1">John Doe</p>
                <p class="text-muted mb-0">john.doe@gmail.com</p>
              </div>
            </div>
          </td>
          <td>
            <p class="fw-bold mb-1">Software engineer</p>
            <p class="text-muted mb-0">IT department</p>
          </td>
          <td>
            <span class="badge badge-success rounded-pill">Active</span>
          </td>
          <td>Senior</td>
          <td>
            <button type="button" class="btn btn-link btn-sm btn-rounded">
              Edit
            </button>
          </td>
        </tr>
        <tr>
          <td>
            <div class="d-flex align-items-center">
              <img
                   src="https://mdbootstrap.com/img/new/avatars/6.jpg"
                   class="rounded-circle"
                   alt=""
                   style="width: 45px; height: 45px"
                   />
              <div class="ms-3">
                <p class="fw-bold mb-1">Alex Ray</p>
                <p class="text-muted mb-0">alex.ray@gmail.com</p>
              </div>
            </div>
          </td>
          <td>
            <p class="fw-normal mb-1">Consultant</p>
            <p class="text-muted mb-0">Finance</p>
          </td>
          <td>
            <span class="badge badge-primary rounded-pill">Onboarding</span>
          </td>
          <td>Junior</td>
          <td>
            <button
                    type="button"
                    class="btn btn-link btn-rounded btn-sm fw-bold"
                    data-mdb-ripple-color="dark"
                    >
              Edit
            </button>
          </td>
        </tr>
        <tr>
          <td>
            <div class="d-flex align-items-center">
              <img
                   src="https://mdbootstrap.com/img/new/avatars/7.jpg"
                   class="rounded-circle"
                   alt=""
                   style="width: 45px; height: 45px"
                   />
              <div class="ms-3">
                <p class="fw-bold mb-1">Kate Hunington</p>
                <p class="text-muted mb-0">kate.hunington@gmail.com</p>
              </div>
            </div>
          </td>
          <td>
            <p class="fw-normal mb-1">Designer</p>
            <p class="text-muted mb-0">UI/UX</p>
          </td>
          <td>
            <span class="badge badge-warning rounded-pill">Awaiting</span>
          </td>
          <td>Senior</td>
          <td>
            <button
                    type="button"
                    class="btn btn-link btn-rounded btn-sm fw-bold"
                    data-mdb-ripple-color="dark"
                    >
              Edit
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

css :

```css
body {
  background-color: hsl(0, 0%, 94%)
}
```

----------

Navbar :

![navbar](/media/ahmedissa/AHMED1/my_important_notes/typora images/navbar.png)

```html
<!-- Navbar-->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid justify-content-between">
    <!-- Left elements -->
    <div class="d-flex">
      <!-- Brand -->
      <a class="navbar-brand me-2 mb-1 d-flex align-items-center" href="#">
        <img
          src="https://mdbcdn.b-cdn.net/img/logo/mdb-transaprent-noshadows.webp"
          height="20"
          alt="MDB Logo"
          loading="lazy"
          style="margin-top: 2px;"
        />
      </a>

      <!-- Search form -->
      <form class="input-group w-auto my-auto d-none d-sm-flex">
        <input
          autocomplete="off"
          type="search"
          class="form-control rounded"
          placeholder="Search"
          style="min-width: 125px;"
        />
        <span class="input-group-text border-0 d-none d-lg-flex"
          ><i class="fas fa-search"></i
        ></span>
      </form>
    </div>
    <!-- Left elements -->

    <!-- Center elements -->
    <ul class="navbar-nav flex-row d-none d-md-flex">
      <li class="nav-item me-3 me-lg-1 active">
        <a class="nav-link" href="#">
          <span><i class="fas fa-home fa-lg"></i></span>
          <span class="badge rounded-pill badge-notification bg-danger">1</span>
        </a>
      </li>

      <li class="nav-item me-3 me-lg-1">
        <a class="nav-link" href="#">
          <span><i class="fas fa-flag fa-lg"></i></span>
        </a>
      </li>

      <li class="nav-item me-3 me-lg-1">
        <a class="nav-link" href="#">
          <span><i class="fas fa-video fa-lg"></i></span>
        </a>
      </li>

      <li class="nav-item me-3 me-lg-1">
        <a class="nav-link" href="#">
          <span><i class="fas fa-shopping-bag fa-lg"></i></span>
        </a>
      </li>

      <li class="nav-item me-3 me-lg-1">
        <a class="nav-link" href="#">
          <span><i class="fas fa-users fa-lg"></i></span>
          <span class="badge rounded-pill badge-notification bg-danger">2</span>
        </a>
      </li>
    </ul>
    <!-- Center elements -->

    <!-- Right elements -->
    <ul class="navbar-nav flex-row">
      <li class="nav-item me-3 me-lg-1">
        <a class="nav-link d-sm-flex align-items-sm-center" href="#">
          <img
            src="https://mdbcdn.b-cdn.net/img/new/avatars/1.webp"
            class="rounded-circle"
            height="22"
            alt="Black and White Portrait of a Man"
            loading="lazy"
          />
          <strong class="d-none d-sm-block ms-1">John</strong>
        </a>
      </li>
      <li class="nav-item me-3 me-lg-1">
        <a class="nav-link" href="#">
          <span><i class="fas fa-plus-circle fa-lg"></i></span>
        </a>
      </li>
      <li class="nav-item dropdown me-3 me-lg-1">
        <a
          class="nav-link dropdown-toggle hidden-arrow"
          href="#"
          id="navbarDropdownMenuLink"
          role="button"
          data-mdb-toggle="dropdown"
          aria-expanded="false"
        >
          <i class="fas fa-comments fa-lg"></i>

          <span class="badge rounded-pill badge-notification bg-danger">6</span>
        </a>
        <ul
          class="dropdown-menu dropdown-menu-end"
          aria-labelledby="navbarDropdownMenuLink"
        >
          <li>
            <a class="dropdown-item" href="#">Some news</a>
          </li>
          <li>
            <a class="dropdown-item" href="#">Another news</a>
          </li>
          <li>
            <a class="dropdown-item" href="#">Something else here</a>
          </li>
        </ul>
      </li>
      <li class="nav-item dropdown me-3 me-lg-1">
        <a
          class="nav-link dropdown-toggle hidden-arrow"
          href="#"
          id="navbarDropdownMenuLink"
          role="button"
          data-mdb-toggle="dropdown"
          aria-expanded="false"
        >
          <i class="fas fa-bell fa-lg"></i>
          <span class="badge rounded-pill badge-notification bg-danger">12</span>
        </a>
        <ul
          class="dropdown-menu dropdown-menu-end"
          aria-labelledby="navbarDropdownMenuLink"
        >
          <li>
            <a class="dropdown-item" href="#">Some news</a>
          </li>
          <li>
            <a class="dropdown-item" href="#">Another news</a>
          </li>
          <li>
            <a class="dropdown-item" href="#">Something else here</a>
          </li>
        </ul>
      </li>
      <li class="nav-item dropdown me-3 me-lg-1">
        <a
          class="nav-link dropdown-toggle hidden-arrow"
          href="#"
          id="navbarDropdownMenuLink"
          role="button"
          data-mdb-toggle="dropdown"
          aria-expanded="false"
        >
          <i class="fas fa-chevron-circle-down fa-lg"></i>
        </a>
        <ul
          class="dropdown-menu dropdown-menu-end"
          aria-labelledby="navbarDropdownMenuLink"
        >
          <li>
            <a class="dropdown-item" href="#">Some news</a>
          </li>
          <li>
            <a class="dropdown-item" href="#">Another news</a>
          </li>
          <li>
            <a class="dropdown-item" href="#">Something else here</a>
          </li>
        </ul>
      </li>
    </ul>
    <!-- Right elements -->
  </div>
</nav>
<!-- Navbar -->
```

