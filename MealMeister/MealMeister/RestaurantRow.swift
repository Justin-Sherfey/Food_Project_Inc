//
//  RestaurantRow.swift
//  Project_Food
//
//  Created by Brett Beattie on 7/8/20.
//  Copyright © 2020 Brett Beattie. All rights reserved.
//

import SwiftUI

struct RestaurantRow: View {
    var loopNumber: Int = 5
    var lopNumber: Int = 4
    
    var body: some View {
        NavigationLink(destination: RestaurantDetail())
        {
            HStack {
                Text("Image")
                VStack(alignment: .leading, spacing: 5) {
                    HStack {
                            Text("Restaurant Name")
                                .font(.headline)
                                .foregroundColor(Color.black)
                        Spacer()
                        //Maybe favorite button??
                        Text("Favorite Button")
                            .foregroundColor(Color.yellow)
                    }
                    HStack {
                        Text("Tags")
                            .foregroundColor(Color.black)
                    }
                    HStack {
                        ForEach(0..<loopNumber) { loopNumber in
                            Image(systemName: "star.fill")
                                .foregroundColor(Color.orange)
                            Spacer(minLength: 10)
                        }
                        ForEach(0..<lopNumber) { loopNumber in
                            Image(systemName: "dollarsign.circle.fill")
                                .foregroundColor(Color.black)
                        }
                        Text("Hours")
                            .foregroundColor(Color.black)
                        //ETA here or with delivery service?
                        Text("ETA")
                            .foregroundColor(Color.black)
                        Spacer()
                        
                    }
                    .font(.subheadline)
                }
            }
        .padding()
        }
    }
}

struct RestaurantRow_Previews: PreviewProvider {
    static var previews: some View {
        RestaurantRow()
            .previewLayout(.fixed(width: 400, height: 100))
    }
}
