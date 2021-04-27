# from mixer.backend.django import mixer
# import pytest

# @pytest.mark.django_db
# class TestModels:

#     def test_price_is_valid(self):
#         # price shouldn't have more than 5 digits including 2 decimal points (max value 999.00)
#         game = mixer.blend('store.Game', price='999')
#         assert game.price == 999.00
#         with pytest.raises(Exception):
#             game = mixer.blend('store.Game', price='1000')
