from Controller.basic import check
from Object.recognition import Recognition

def recognition(cn, nextc):
     if cn.req.files.get('voice') is None:
        return cn.toret.add_error(400, "Missing voice file")
    err = Recognition().totext(voice=cn.req.files.get('voice'))
    return cn.call_next(nextc, err)
