import trafaret as t


def D(x): return t.Dict(x).allow_extra('*')


schema = D({t.Key('queryType'): D({t.Key('name'):         t.String()}),
            t.Key('mutationType'): t.Null(),
            t.Key('subscriptionType'): t.Null(),
            t.Key('types'):     t.List(D({t.Key('kind'):     t.String(),
                                          t.Key('name'):     t.String(),
                                          t.Key('description'): t.Null(),
                                          t.Key('fields'):     t.List(D({t.Key('name'):     t.String(),
                                                                         t.Key('description'): t.Null(),
                                                                         t.Key('args'):     t.List(D({t.Key('name'):     t.String(),
                                                                                                      t.Key('description'): t.Null(),
                                                                                                      t.Key('type'): D({t.Key('kind'):         t.String(),
                                                                                                                        t.Key('name'):         t.String(),
                                                                                                                        t.Key('ofType'): t.Null()}
                                                                                                                       ),
                                                                                                      t.Key('defaultValue'): t.Null()}
                                                                                                     )),
                                                                         t.Key('type'): D({t.Key('kind'):         t.String(),
                                                                                           t.Key('name'):         t.String(),
                                                                                           t.Key('ofType'): t.Null()}
                                                                                          ),
                                                                         t.Key('isDeprecated'):     t.Int(),
                                                                         t.Key('deprecationReason'): t.Null()}
                                                                        )),
                                          t.Key('inputFields'): t.Null(),
                                          t.Key('interfaces'):     t.List(t.Any()),
                                          t.Key('enumValues'): t.Null(),
                                          t.Key('possibleTypes'): t.Null()}
                                         )),
            t.Key('directives'):     t.List(D({t.Key('name'):     t.String(),
                                               t.Key('description'):     t.String(),
                                               t.Key('args'):     t.List(D({t.Key('name'):     t.String(),
                                                                            t.Key('description'):     t.String(),
                                                                            t.Key('type'): D({t.Key('kind'):         t.String(),
                                                                                              t.Key('name'): t.Null(),
                                                                                              t.Key('ofType'): D({t.Key('kind'):             t.String(),
                                                                                                                  t.Key('name'):             t.String(),
                                                                                                                  t.Key('ofType'): t.Null()}
                                                                                                                 )}
                                                                                             ),
                                                                            t.Key('defaultValue'): t.Null()}
                                                                           )),
                                               t.Key('onOperation'):     t.Int(),
                                               t.Key('onFragment'):     t.Int(),
                                               t.Key('onField'):     t.Int()}
                                              ))}
           )
