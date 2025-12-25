from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart


# GET 요청: OrderCreateForm 폼을 인스턴스화하고 create.html 템플릿을 렌더링한다.
# POST 요청: 전송된 데이터의 유효성을 검사한다. 데이터가 유효하면 order = form.save()를 사용하여 데이터베이스에 새로운 주문을 생성한다.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()

            # 작업의 delay() 메서드를 호출해서 작업을 비동기적으로 실행한다.
            order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
