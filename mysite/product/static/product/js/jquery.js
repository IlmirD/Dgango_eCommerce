$(document).ready(function(){
    var form = $('#add_product_to_cart');
    // Adding to cart
    form.on('submit', function(e){
        e.preventDefault();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');

        var data = {};
        data.product_id = product_id;
        var csrf_token = $('#add_product_to_cart [name="csrfmiddlewaretoken"]').val();
        data['csrfmiddlewaretoken'] = csrf_token;

        var url = form.attr('action');

        $.ajax({
            url: url,
            type:'POST',
            data: data,
            success: function(data){
                    if (data.new_total){
                        $('#quantity').text(data.new_total);
                    }
                },
                error: function(){
                    console.log('Error');
                }
        });
    });

    
    var updateBtns = $('.update-cart');
    // updating the quantity
    for (i = 0; i < updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(e){
            e.preventDefault();
            var productID = this.dataset.product;
            var action = this.dataset.action;
            console.log(productID);
            console.log(action);

            var class_name = productID.toString();
            console.log('class name:', class_name);

            var data = {};
            data.product_id = productID;
            data.action = action;
            var csrf_token = $('#update_cart [name="csrfmiddlewaretoken"]').val();
            data['csrfmiddlewaretoken'] = csrf_token;
    
            var url = '/cart/';
            $.ajax({
                url: url,
                type:'POST',
                data: data,
                success: function(data){
                            console.log('success');
                            $("." + class_name).load(location.href + " ." + class_name);
                            $('#total').load(location.href + ' #total');
                    },
                    error: function(){
                        console.log('Error');
                    }
            });

        });
    }

});