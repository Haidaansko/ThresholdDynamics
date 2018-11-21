c = get_config()
c.NbConvertApp.export_format = 'pdf'
c.TemplateExporter.template_path = ['.']
c.Exporter.template_file = 'article'
