class ProcessingBase:
    def preproccess(self, *args, **kwargs):
        raise NotImplementedError("Method \'preproccess\' is not implemented\
                                  for this class.")

    def postprocess(self, *args, **kwargs):
        NotImplementedError("Method \'postproccess\' is not implemented\
                                  for this class.")