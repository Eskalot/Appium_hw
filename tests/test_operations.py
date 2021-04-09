
class TestCalculator:

    def test_add_value(self, calculator):
        calculator.add_values(1, 2)
        result = calculator.get_result()
        assert int(result) == 3
        """ można też zastosować krótszy kod i zamiast tworzyć zmienną result od razu zastosować asercję:  
        assert int(calculator.get_result()) == 3
        """


    def test_divide_value(self, calculator):
        calculator.divide_values(1, 2)
        result = calculator.get_result()
        assert float(result) == 0.5

    def test_sub_value_positive(self, calculator):
        calculator.sub_values(5, 1)
        result = calculator.get_result()
        assert result == "4"

    def test_sub_value_negative(self, calculator):
        calculator.sub_values(1, 5)
        result = calculator.get_result()
        assert result == "-4"

    def test_divide_by_zero(self, calculator):
        calculator.divide_values(4, 0)
        result = calculator.get_result_if_0()
        assert result == "Can't divide by 0"


    def test_clear_result(self,calculator):
        calculator.clear_result()


    def test_open_panel_expert(self, calculator):
        calculator.open_expert_panel()


    def test_close_panel_expert(self, calculator):
        calculator.close_expert_panel()


    def test_calculate_sinus(self,calculator):
        calculator.calculate_sinus(4,5)
        result = calculator.get_result()
        assert float(result) == 0.7071067811


