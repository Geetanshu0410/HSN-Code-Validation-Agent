class Intent:
    def __init__(self, name, example_phrases):
        self.name = name
        self.examples = example_phrases

ValidateCode = Intent(
    name="ValidateCode",
    example_phrases=[
        "Check HSN code {HSNCode}",
        "Is {HSNCode} a valid HSN code?",
        "Validate code {HSNCode}"
    ]
)