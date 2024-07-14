from flask import Blueprint, jsonify, request
from ..models import db, Visitor

bp = Blueprint('api', __name__)

@bp.route('/api/', methods=['GET'])
def index():
    try:
        ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
        new_visitor = Visitor(ip=ip)
        db.session.add(new_visitor)
        db.session.commit()
        unique_visitors = db.session.query(db.func.count(db.distinct(Visitor.ip))).scalar()
        return jsonify(unique_visitors=unique_visitors)
    except Exception as e:
        return jsonify(error=str(e)), 500

@bp.route('/api/version', methods=['GET'])
def version():
    return jsonify({"version": "1.0.0"})

@bp.route('/api/reportcode', methods=['GET'])
def report_code():
    import subprocess
    import json
    try:
        autopep8_result = subprocess.run(
            ['autopep8', '/app/app.py', '-v', '-i'],
            capture_output=True,
            text=True,
            check=True
        )

        pylint_result = subprocess.run(
            ['pylint', '--rcfile=/app/.pylintrc', 'app'],
            capture_output=True,
            text=True,
            check=True
        )

        report = {
            'pylint': {
                'returncode': pylint_result.returncode,
                'stdout': pylint_result.stdout.splitlines(),
                'stderr': pylint_result.stderr.splitlines(),
            },
            'autopep8': {
                'returncode': autopep8_result.returncode,
                'stdout': autopep8_result.stdout.splitlines(),
                'stderr': autopep8_result.stderr.splitlines(),
            }
        }
        return jsonify(report)
    except subprocess.CalledProcessError as e:
        return jsonify(error=str(e)), 500
    except Exception as e:
        return jsonify(error=f"Unexpected error: {str(e)}"), 500

