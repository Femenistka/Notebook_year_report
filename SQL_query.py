# class SQL_stat () : 
    
class SQLQueries:

    @staticmethod
    def get_expenses_by_week():
        return """
        SELECT 
        SUM("Сумма в валюте счета") AS 'Сумма',
        strftime('%W', "Дата и время") AS 'Номер недели'
        FROM Expenses
        WHERE `Категория` NOT IN ('Купил (основная сумма)', 'Другое', 'Дал в долг')
        GROUP BY strftime('%W', "Дата и время")
        ORDER BY strftime('%W', "Дата и время");
        """
    
    def get_income_by_week():
        return """
        SELECT 
        SUM("Сумма в валюте счета") AS 'Сумма',
        strftime('%W', "Дата и время") AS 'Номер недели'
        FROM Income
        WHERE `Категория` IN ('Работа', 'Прибыль с продажи')
        GROUP BY strftime('%W', "Дата и время")
        ORDER BY strftime('%W', "Дата и время");
        """
    
    @staticmethod
    def get_expenses_by_month():
        return """
        SELECT 
            strftime('%m', "Дата и время") AS "Месяц",
            SUM("Сумма в валюте счета") AS "Сумма в валюте счета",
            Категория
        FROM 
            expenses
        WHERE 
            Категория IN ('Кафе', 'Досуг', 'Подарки', 'Мое ведро', 'Продукты', 
                         'Такси', 'Одежда', 'Каршеринг', 'Университет', 'Штрафы', 
                         'Здоровье')
        GROUP BY 
            "Месяц", Категория
        ORDER BY 
            "Месяц";
        """

    @staticmethod
    def get_total_expenses_by_month():
        return """
        SELECT 
            strftime('%m', "Дата и время") AS "Месяц",
            SUM("Сумма в валюте счета") AS "Сумма в валюте счета"
        FROM 
            expenses
        WHERE 
            Категория IN ('Кафе', 'Досуг', 'Подарки', 'Мое ведро', 'Продукты', 
                         'Такси', 'Одежда', 'Каршеринг', 'Университет', 'Штрафы', 
                         'Здоровье')
        GROUP BY 
            "Месяц"
        ORDER BY 
            "Месяц";
        """

    @staticmethod
    def get_top_expenses_categories():
        return """
        WITH RankedCategories AS (
            SELECT 
                Категория,
                SUM("Сумма в валюте счета") AS "Общая сумма",
                ROW_NUMBER() OVER (ORDER BY SUM("Сумма в валюте счета") DESC) as rank
            FROM 
                expenses
            WHERE 
                Категория NOT IN ("Купил (основная сумма)", "Другое", "Дал в долг")
            GROUP BY 
                Категория
        )
        SELECT 
            CASE 
                WHEN rank <= 5 THEN Категория
                ELSE 'Прочее...'
            END as Категория,
            SUM("Общая сумма") as "Общая сумма"
        FROM 
            RankedCategories
        GROUP BY 
            CASE 
                WHEN rank <= 5 THEN Категория
                ELSE 'Прочее...'
            END
        ORDER BY 
            SUM("Общая сумма") DESC;
        """

    @staticmethod
    def get_total_expenses_by_category():
        return """
        SELECT 
            Категория,
            SUM("Сумма в валюте счета") AS "Общая сумма"
        FROM 
            expenses
        GROUP BY 
            Категория
        ORDER BY 
            "Общая сумма" DESC;
        """

    @staticmethod
    def get_monthly_income():
        return """
        SELECT 
            strftime('%m', "Дата и время") AS "Месяц",
            SUM("Сумма в валюте счета") AS "Сумма в валюте счета"
        FROM 
            income
        WHERE 
            Категория IN ('Прибыль с продажи', 'Работа')
        GROUP BY 
            "Месяц"
        ORDER BY 
            "Месяц";
        """
    
    @staticmethod
    def get_total_income():
        return """
        SELECT 
            SUM("Сумма в валюте счета") AS "Сумма в валюте счета",
            Категория
        FROM 
            income
        WHERE 
            Категория IN ('Прибыль с продажи', 'Работа')
        GROUP BY
           Категория 
        """
    
    @staticmethod
    def get_monthly_comparison():
        return """
        WITH expenses_data AS (
            SELECT 
                strftime('%m', "Дата и время") AS "Месяц",
                COALESCE(SUM("Сумма в валюте счета"), 0) AS "Расходы"
            FROM 
                expenses
            WHERE 
                Категория IN ('Кафе', 'Досуг', 'Подарки', 'Мое ведро', 'Продукты', 
                             'Такси', 'Одежда', 'Каршеринг', 'Университет', 'Штрафы', 
                             'Здоровье')
            GROUP BY 
                "Месяц"
        ),
        income_data AS (
            SELECT 
                strftime('%m', "Дата и время") AS "Месяц",
                COALESCE(SUM("Сумма в валюте счета"), 0) AS "Доходы"
            FROM 
                income
            WHERE 
                Категория IN ('Прибыль с продажи', 'Работа')
            GROUP BY 
                "Месяц"
        )
        SELECT 
            e."Месяц",
            COALESCE(e."Расходы", 0) AS "Расходы",
            COALESCE(i."Доходы", 0) AS "Доходы",
            COALESCE(i."Доходы", 0) - COALESCE(e."Расходы", 0) AS "Сбережения"
        FROM 
            expenses_data e
        LEFT JOIN 
            income_data i ON e."Месяц" = i."Месяц"
        ORDER BY 
            e."Месяц";
        """

    @staticmethod
    def get_income_by_student():
        return """
        SELECT 
            "Теги" as "Ученик",
            SUM("Сумма в валюте счета") as "Сумма"
        FROM 
            income
        WHERE 
            "Теги" IN ('Максим', 'Варвара', 'Иван', 'Марат')
            AND "Категория" IN ('Прибыль с продажи', 'Работа')
        GROUP BY 
            "Теги"
        ORDER BY 
            "Сумма" DESC;
        """

    @staticmethod
    def get_income_by_goods():
        return """
        SELECT 
            "Теги" as "Товар",
            SUM("Сумма в валюте счета") as "Сумма"
        FROM 
            income
        WHERE 
            "Теги" IN ('YAMAHA', 'Casio')
            AND "Категория" IN ('Прибыль с продажи')
        GROUP BY 
            "Теги"
        ORDER BY 
            "Сумма" DESC;
        """
    
    @staticmethod
    def expenses_by_transport():
        return """
        SELECT 
        "Теги" as "Транспорт",
            SUM("Сумма в валюте счета") as "Сумма"
        FROM 
            Expenses
        WHERE 
            "Теги" IN ('84', '53', '116', 'Другой транспорт')
        GROUP BY 
            "Теги"
        ORDER BY 
            "Сумма" DESC;

        """

    @staticmethod
    def get_transactions_by_date_range(start_date, end_date):
        return f"""
        SELECT 
            "Дата и время",
            "Тип операции",
            "Сумма в валюте счета",
            Категория,
            "Описание"
        FROM 
            transactions
        WHERE 
            "Дата и время" BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY 
            "Дата и время";
        """ 