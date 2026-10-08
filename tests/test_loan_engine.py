import unittest
from app.loan_engine import determine_loans

class LoanEngineTest(unittest.TestCase):
    def types(self, age, income, location):
        return [item["type"] for item in determine_loans(age, income, location)]

    def test_baixa_renda_leva_pessoal_e_garantido(self):
        self.assertEqual(self.types(40, 3000, "RJ"), ["PERSONAL", "GUARANTEED"])

    def test_jovem_de_sp_na_faixa_do_meio(self):
        self.assertEqual(self.types(29, 4500, "SP"), ["PERSONAL", "GUARANTEED"])

    def test_renda_alta_so_consignado(self):
        self.assertEqual(self.types(26, 7000, "SP"), ["CONSIGNMENT"])

if __name__ == "__main__":
    unittest.main()
