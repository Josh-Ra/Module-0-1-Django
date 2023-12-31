from django.test import SimpleTestCase

# Create your tests here.
class NearOneHundred(SimpleTestCase):
    def test_NearOneHundred_Ten(self):
        response = self.client.get("/near-hundred/10")
        self.assertContains(response, False)

    def test_NearHundred_90(self):
        response = self.client.get("/near-hundred/90")
        self.assertContains(response, True)

    def test_NearHundred_110(self):
        response = self.client.get("/near-hundred/110")
        self.assertContains(response, True)

class StringSplosion(SimpleTestCase):
    def test_string_splosion_code(self):
        response = self.client.get("/string-splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_string_splosion_abc(self):
        response = self.client.get("/string-splosion/abc")
        self.assertContains(response, "aababc")

    def test_string_splosion_ab(self):
        response = self.client.get("/string-splosion/abc")
        self.assertContains(response, "aab")

class CatDog(SimpleTestCase):
    def test_cat_dog_catcatdog(self):
        response = self.client.get("/cat-dog/catcatdog")
        self.assertContains(response, False)

    def test_cat_dog_dogdogcat(self):
        response = self.client.get("/cat-dog/dogdogcat")
        self.assertContains(response,False)
    
    def test_cat_dog_dogdogcatcatatogat(self):
        response = self.client.get("/cat-dog/dogdogcatcatatogat")
        self.assertContains(response,True)

class LoneSum(SimpleTestCase):
    def test_lone_sum_1_2_3(self):
        response = self.client.get("/lone-sum/1/2/3")
        self.assertContains(response, 6)

    def test_lone_sum_2_2_3(self):
        response = self.client.get("/lone-sum/2/2/3")
        self.assertContains(response, 3)

    def test_lone_sum_3_3_3(self):
        response = self.client.get("/lone-sum/3/3/3")
        self.assertContains(response, 0)