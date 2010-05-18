class Defect(models.Model):
    """
    A defect filed upon a review request.

    """
    filediff = models.ForeignKey(FileDiff, verbose_name=_('file diff'),
                                 related_name="comments")
    interfilediff = models.ForeignKey(FileDiff,
                                      verbose_name=_('interdiff file'),
                                      blank=True, null=True,
                                      related_name="interdiff_comments")

    timestamp = models.DateTimeField(_('timestamp'), default=datetime.now)
    text = models.TextField(_("comment text"))

    class Meta:
        ordering = ['timestamp']
