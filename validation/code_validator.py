from data.loader import load_hsn_data

class HSNValidator:
    def __init__(self):
        self.hsn_data = load_hsn_data()

    def validate(self, code: str):
        code = (code or "").strip()
        if not code:
            return False, "Please enter an HSN code."
        if not code.isdigit():
            return False, "Invalid format: HSN code must be numeric."
        if len(code) < 2 or len(code) > 8:
            return False, "Invalid format: length must be 2 to 8 digits."
        if code not in self.hsn_data:
            return False, "HSN code not found in the master data."

        parents = [code[:i] for i in range(2, len(code), 2)]
        missing = [p for p in parents if p and p not in self.hsn_data]
        if missing:
            return False, f"Incomplete hierarchy: missing parent code(s) {missing}."
        desc = self.hsn_data.get(code, "")
        return True, f"Valid HSN code. Description: {desc}"