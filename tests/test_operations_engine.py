import unittest

from src.realestate_ops.validator import validate_records
from src.realestate_ops.daily_report import build_daily_report, render_markdown


class ValidatorTests(unittest.TestCase):
    def test_qualified_requires_next_action(self):
        records = [{
            "record_id": "T-001",
            "organization_or_person": "Example LLC",
            "business_reason": "Verified relationship",
            "stage": "Qualified",
            "compliance_status": "Clear",
            "dnc_opt_out": False,
        }]
        report = validate_records(records)
        self.assertFalse(report.valid)
        self.assertTrue(any(i.rule_id == "R001" for i in report.issues))

    def test_compliance_review_routes_to_compliance(self):
        records = [{
            "record_id": "T-002",
            "organization_or_person": "Example LLC",
            "business_reason": "Verified relationship",
            "stage": "Opportunity",
            "compliance_status": "Review Required",
            "next_action": "Review activity",
            "next_action_date": "2026-09-21",
            "dnc_opt_out": False,
        }]
        report = validate_records(records)
        self.assertFalse(report.valid)
        self.assertIn("T-002", report.queues()["compliance"])

    def test_won_requires_revenue_evidence(self):
        records = [{
            "record_id": "T-003",
            "organization_or_person": "Example LLC",
            "business_reason": "Verified relationship",
            "stage": "Won",
            "compliance_status": "Clear",
            "actual_revenue": 0,
            "revenue_date": "2026-09-18",
            "dnc_opt_out": False,
        }]
        report = validate_records(records)
        self.assertFalse(report.valid)
        self.assertIn("T-003", report.queues()["revenue"])

    def test_dnc_suppresses_outreach(self):
        records = [{
            "record_id": "T-004",
            "organization_or_person": "Example LLC",
            "business_reason": "Verified relationship",
            "stage": "New",
            "compliance_status": "Clear",
            "dnc_opt_out": True,
        }]
        report = validate_records(records)
        self.assertTrue(report.valid)
        self.assertIn("T-004", report.queues()["suppression"])

    def test_daily_report_is_renderable(self):
        report = validate_records([])
        daily = build_daily_report(report, today="2026-09-18")
        markdown = render_markdown(daily)
        self.assertIn("2026-09-18", markdown)
        self.assertIn("Records checked", markdown)


if __name__ == "__main__":
    unittest.main()
