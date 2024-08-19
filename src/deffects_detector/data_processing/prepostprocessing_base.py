class ProcessingBase:
    def preproccess(self, data):
        raise NotImplementedError("Method \'preproccess\' is not implemented\
                                  for this class.")

    def postprocess(self, data):
        NotImplementedError("Method \'postproccess\' is not implemented\
                                  for this class.")