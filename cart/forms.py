from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # 입력값을 정수로 변환하기 위해 coerce=int 로 설정한 TypedChoiceField 필드를 사용한다.
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)

    # 이 제품의 카트에 있는 기존 수량에 주어진 수량을 추가할지 또는 기존 수량을 주어진 수량으로 덮어 쓸지 를 표시할 수 있다.
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
