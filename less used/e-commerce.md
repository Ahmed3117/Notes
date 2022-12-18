# Apps :

* ### accounts :

  * #### User :

    * first_name
    * last_name
    * mail
    * phone
    * first_address
    * second_address (special place near to your address )
    * country
    * zip_code

* ### about :

  * #### About :

    * name
    * logo
    * description
    * phone
    * mail
    * address

  * #### Country : (countries that we can deliver to them):

    * name

* ### products :

  * #### Category :

    * name

  * #### Sub Category :

    * name
    * category (foreign key with Category)

  * #### Brand :

    * logo
    * name

  * #### Product :

    * image (to show them in slider in product details , use a random one to be main image to the product)
    * category (foreign key with Category)
    * name
    * brand (foreign key with Brand)
    * current_price
    * previous_price
    * description

  * #### AvailableSizes :

    * size_name
    * available_quantity
    * product (Foreign Key relationship with Product)

  * #### AvilaableColors :

    * color_name
    * available_quantity
    * product (Foreign Key relationship with Product)

  * #### Product_Images :

    * image
    * product (Many To Many relationship with Product)

  * ### Review :

    * user
    * product
    * comment
    * star_number

  * #### Cart :

    * user
    * product
    * quantity

  * #### Love :

    * user
    * product

* ### contact :

  * #### Contact :

    * name
    * mail
    * subject
    * message