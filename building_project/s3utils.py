from storages.backends.s3boto import S3BotoStorage

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')

# class StaticRootS3BotoStorage(S3BotoStorage):
#     location = 'static'
#
#
# class MediaRootS3BotoStorage(S3BotoStorage):
#     location = 'media'