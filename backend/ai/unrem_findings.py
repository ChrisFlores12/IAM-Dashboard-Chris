from database_service import DatabaseService

# the goal of this script is to gather all the findings from the IAM dashboard security scans and organize them into a dictionary of findings.
# using the database service file, we can gather all the findings from the database and organize them into a dictionary of findings.
# using that dictionary of findings, we can pair them to an issue and generate a remedation method in another file.

db_service = DatabaseService()

finding_dict = {
    'security_findings': {
        'total': total_findings,
        'critical': critical_findings,
        'high': high_findings,
        'resolved': resolved_findings
    },
    'compliance': {
        'total_resources': 0,
        'compliant': 0,
        'non_compliant': 0
    }
}

security_findings = db_service.get_security_findings()

def organize_findings(findings: list[SecurityFinding]) -> dict:
    findings_dict = {}
    for finding in findings:
        findings_dict[finding.id] = finding
    return findings_dict

