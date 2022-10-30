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

